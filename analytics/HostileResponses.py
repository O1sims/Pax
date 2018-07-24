import os

import pymongo as pm

from analytics.UnitAnalysis import get_hostile_unit
from analytics.ActionAnalysis import action_force
from analytics.Criticality import calculate_asset_criticality
from analytics.Config import risk_label_from_score, probability_label_from_score, threat_label_level_map
from analytics.SystemAnalysis import number_of_vulnerabilities, number_of_threats, asset_from_id


def get_counter_effects(effect, effect_type):
    client = pm.MongoClient(
        host=os.environ.get('DB_HOSTNAME'),
        port=int(os.environ.get('DB_PORT'))
    )
    hostile_response_collection = client[os.environ.get('DB_NAME')]['hostile_response']
    hostile_responses = list(hostile_response_collection.find({"effect": effect}, {"_id": 0}))
    counter_effect = hostile_responses[0]['hostileResponse'][effect_type]
    return counter_effect


def get_effect_likeliness(assets, asset_id, effect):
    asset_type = get_asset_type(
        assets=assets,
        asset_id=asset_id
    )
    client = pm.MongoClient(
        host=os.environ.get('DB_HOSTNAME'),
        port=int(os.environ.get('DB_PORT'))
    )
    action_list_collection = client[os.environ.get('DB_NAME')]['action_list']
    effect_detail = list(action_list_collection.find(
        {
            "force": "hostile",
            "effect": effect,
            "type": asset_type
        }, {
            "_id": 0
        }))
    likeliness = effect_detail[0]['properties']["likeliness"]
    return likeliness


def generate_response(system_data, effect, objective, impact, probability, hostile_unit, risk_score_after):
    counter_response = {
        'actions': get_counter_actions(
            assets=system_data['assets'],
            objective=objective,
            effect=effect,
            force="hostile"
        ),
        'effect': effect,
        'objective': objective,
        'impactScore': impact,
        'impactLabel': risk_label_from_score(
            risk_score=impact
        ),
        'actor': hostile_unit['id'],
        'probabilityOfSuccessScore': probability,
        'probabilityOfSuccessScoreLabel': probability_label_from_score(
            probability=probability
        ),
        'riskScoreAfter': risk_score_after,
        'riskLabelAfter': risk_label_from_score(
            risk_score=risk_score_after
        ),
        'description': get_counter_description(
            system_data=system_data,
            objective=objective,
            impact=impact,
            hostile_unit=hostile_unit,
            effect=effect,
            probability=probability
        )
    }
    return counter_response


def get_counter_description(system_data, objective, hostile_unit, effect, probability, impact):
    hostile_effect = effect
    asset = asset_from_id(
        asset_id=objective,
        assets=system_data['assets'],
        asset_type=False
    )
    vuln_no = number_of_vulnerabilities(
        asset_id=asset['id'],
        vulnerabilities=system_data['vulnerabilities']
    )
    effects_capability_label = threat_label_level_map(
        threat_level=hostile_unit['effectsCapability']
    )
    probability_label = probability_label_from_score(
        probability=probability
    )
    impact_label = risk_label_from_score(
        risk_score=impact
    )
    if vuln_no == 1:
        v = "vulnerability"
    else:
        v = "vulnerabilities"
    desc = "The hostile unit " + hostile_unit['name'] + ", known to have a " + effects_capability_label + \
           " capability level will " + \
           hostile_effect + " the " + asset['name']
    if vuln_no == 0:
        desc = desc + "."
    else:
        desc = desc + ", which is known to have " + str(vuln_no) + " " + v + "."
    if hostile_effect == 'SECURE':
        desc += " By securing the asset any known vulnerabilities will be patched and removed."
    elif hostile_effect == 'DESTROY':
        desc += " By destroying the asset, the impact on the current mission will be High."
    desc += " The " + hostile_unit['name'] + " will achieve this counter-action with a " + probability_label + \
            " (" + str(probability) + "%) probability."
    return desc


def get_counter_actions(assets, objective, effect, force="hostile"):
    asset_type = get_asset_type(
        assets=assets,
        asset_id=objective
    )
    client = pm.MongoClient(
        host=os.environ.get('DB_HOSTNAME'),
        port=int(os.environ.get('DB_PORT'))
    )
    action_list_collection = client[os.environ.get('DB_NAME')]['action_list']
    action_data = action_list_collection.find_one({
        "force": force,
        "effect": effect,
        "type": asset_type
    }, {
        "_id": 0
    })
    counter_actions = action_data['actions']
    return counter_actions


def get_asset_type(assets, asset_id):
    for asset in assets:
        if asset['id'] == asset_id:
            return asset['assetType'].lower()


def get_most_dangerous_target_asset(system_data, most_likely):
    max_target_score = 0
    cyber_physical_assets = filter_assets(
        assets=system_data['assets'],
        asset_types=[
            'physical',
            'cyber'
        ]
    )
    for asset in cyber_physical_assets:
        if asset['id'] is not most_likely:
            criticality = calculate_asset_criticality(
                asset=asset
            )
            no_of_vulnerabilities = number_of_vulnerabilities(
                asset_id=asset['id'],
                vulnerabilities=system_data['vulnerabilities']
            )
            no_of_threats = number_of_threats(
                asset_id=asset['id'],
                threats=system_data['threats']
            )
            if no_of_threats == 0:
                target_score = criticality * no_of_vulnerabilities
            else:
                target_score = criticality * no_of_threats * no_of_vulnerabilities
            if target_score >= max_target_score:
                max_target_score = target_score
                most_dangerous_target_asset = asset
    return most_dangerous_target_asset


def get_most_likely_target_asset(system_data):
    max_vulnerabilities = 0
    cyber_physical_assets = filter_assets(
        assets=system_data['assets'],
        asset_types=[
            'physical',
            'cyber'
        ]
    )
    for asset in cyber_physical_assets:
        no_of_vulnerabilities = number_of_vulnerabilities(
            asset_id=asset['id'],
            vulnerabilities=system_data['vulnerabilities']
        )
        if no_of_vulnerabilities >= max_vulnerabilities:
            max_vulnerabilities = system_data['vulnerabilities']
            most_likely_target_asset = asset
    return most_likely_target_asset


def filter_assets(assets, asset_types):
    filtered_assets = []
    for asset in assets:
        if asset['assetType'].lower() in asset_types:
            filtered_assets.append(asset)
    return filtered_assets


class HostileResponses:
    def __init__(self, system_data):
        self.system_data = system_data

    def get_response(self, action, risk_score, asset_id, most_likely=False, most_dangerous=False, most_likely_asset=None):
        hostile_unit = get_hostile_unit()
        if most_likely:
            counter_effect = get_counter_effects(
                effect=action['effect'],
                effect_type="mostLikely"
            )
            most_asset = get_most_likely_target_asset(
                system_data=self.system_data
            )
            if most_asset['id'] == asset_id:
                most_risk = 100 - max(24, min(100, risk_score - 20))
            else:
                most_risk = 100 - min(100, max(36, risk_score - 30))
        if most_dangerous:
            counter_effect = get_counter_effects(
                effect=action['effect'],
                effect_type="mostDangerous"
            )
            most_asset = get_most_dangerous_target_asset(
                system_data=self.system_data,
                most_likely=most_likely_asset
            )
            if most_asset['id'] == asset_id:
                most_risk = 100 - max(22, min(100, risk_score + 20))
            else:
                most_risk = 100 - min(100, max(20, risk_score - 50))
        impact = calculate_asset_criticality(
            asset=most_asset
        )
        probability_of_success = self.get_probability_of_counter_effect_success(
            counter_effect=counter_effect,
            asset=most_asset,
            most_likely=most_likely
        )
        response = generate_response(
            effect=counter_effect,
            objective=most_asset['id'],
            impact=impact,
            hostile_unit=hostile_unit,
            probability=probability_of_success,
            risk_score_after=most_risk,
            system_data=self.system_data
        )
        if most_likely and most_dangerous:
            all_responses = {
                'most_likely': most_likely,
                'most_dangerous': most_dangerous
            }
            return all_responses
        return response

    def get_probability_of_counter_effect_success(self, asset, counter_effect, most_likely=False):
        counter_effect = counter_effect.upper()
        counter_force = action_force(
            effect=counter_effect
        )
        if most_likely:
            unit_success = 80
        else:
            unit_success = 20
        effect_likeliness = get_effect_likeliness(
            assets=self.system_data['assets'],
            asset_id=asset['id'],
            effect=counter_effect
        )
        all_vuln_no = len(self.system_data['vulnerabilities'])
        vuln_no = number_of_vulnerabilities(
            asset_id=asset['id'],
            vulnerabilities=self.system_data['vulnerabilities']
        )
        vuln_ratio = int(100 * (float(vuln_no)/max(1, all_vuln_no)))
        if counter_force == 'defensive':
            normalised_vulnerability = 100 - vuln_ratio
        elif counter_force == 'offensive':
            normalised_vulnerability = 100 - vuln_ratio
        probabiliy_counter_effect = int((0.2 * unit_success) + (0.3 * normalised_vulnerability) + (0.5 * effect_likeliness))
        return probabiliy_counter_effect

