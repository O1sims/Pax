import os
import requests

import pymongo as pm

from analytics.UnitAnalysis import get_unit_data
from analytics.Config import threat_label_level_map
from utils import SystemConfig as config


def get_mission_data_from_system_id(system_id, id_only=False):
    get_missions = requests.get('http://{}missions'.format(config.C2_REST))
    missions = get_missions.json()

    for mission in missions:
        get_mission = requests.get('http://{}missions/{}'.format(config.C2_REST, mission['globalId']))
        mission_data = get_mission.json()
        if mission_data['systems'][0]['id'] == system_id:
            if not id_only:
                return mission_data
            else:
                return mission_data['globalId']


def get_asset_coordinates(mission_data, asset_id):
    for overlay in mission_data['overlays']:
        for drawing in overlay['drawings']:
            if drawing['represents']['entityId'].lower() == asset_id.lower():
                layer_type = drawing['feature']['properties']['layerType'].lower()
                radius = None
                coordinates = drawing['feature']['geometry']['coordinates']
                if layer_type == 'circle':
                    radius = drawing['feature']['properties']['radius']
                    inverted_coordinates = [coordinates[1], coordinates[0]]
                    latitude = inverted_coordinates[0]
                    longitude = inverted_coordinates[1]
                elif layer_type == 'polygon':
                    inverted_coordinates = []
                    for coordinate in coordinates[0]:
                        inverted_coordinates.append([coordinate[1], coordinate[0]])
                    latitude = inverted_coordinates[0][0]
                    longitude = inverted_coordinates[0][1]
                elif layer_type == 'point':
                    radius = 10
                    inverted_coordinates = [coordinates[1], coordinates[0]]
                    latitude = inverted_coordinates[0]
                    longitude = inverted_coordinates[1]
                elif layer_type == 'polyline':
                    inverted_coordinates = []
                    for coordinate in coordinates:
                        inverted_coordinates.append([coordinate[1], coordinate[0]])
                    latitude = inverted_coordinates[0][0]
                    longitude = inverted_coordinates[0][1]
                location_object = {
                    'latitude': latitude,
                    'longitude': longitude,
                    'drawing': inverted_coordinates,
                    'layerType': layer_type,
                    'radius': radius
                }
                return location_object


def system_geolocation(system_id):
    r = requests.get('http://{}missions'.format(config.C2_REST))
    missions = r.json()
    for mission in missions:
        r = requests.get('http://{}missions/{}'.format(config.C2_REST, mission['globalId']))
        mission_data = r.json()
        if mission_data['systems'][0]['id'] == system_id:
            bbox = mission_data['bbox']
            coordinates = [float(i) for i in bbox.split(",")]
            mission_coordinates = {
                'longitude': (coordinates[0] + coordinates[2]) / 2,
                'latitude': (coordinates[1] + coordinates[3]) / 2
            }
            return mission_coordinates


def offensive_or_defensive(action_effect):
    client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
    effects_collection = client[os.environ.get('DB_NAME')]['hostile_response']
    effect_info = effects_collection.find_one({"effect": action_effect})
    force = effect_info['effectType']
    return force


def remove_asset_vulnerabilities(system_data, action_data):
    vulnerability_ids_to_remove = []

    for action in action_data:
        if action['effect'].upper() == 'MOVE':
            continue

        if offensive_or_defensive(action['effect'].upper()) == 'defensive':
            action_asset = action['objective']

            for vulnerability in system_data['vulnerabilities']:
                if action_asset in vulnerability['assets']:
                    vulnerability_ids_to_remove.append(vulnerability['id'])

    if len(vulnerability_ids_to_remove) > 0:
        unique_vulnerability_ids = list(set(vulnerability_ids_to_remove))
        for vid in unique_vulnerability_ids:
            for vulnerability in system_data['vulnerabilities']:
                if vulnerability['id'] == vid:
                    system_data['vulnerabilities'].remove(vulnerability)

    return system_data


def add_asset_threats(system_data, action_data):
    threats_to_add = []
    for action in action_data:
        if action['effect'].upper() == 'MOVE':
            continue

        if offensive_or_defensive(action['effect'].upper()) == 'offensive':
            unit_data = get_unit_data(unit_id=action['actor'])
            threat_capability = threat_label_level_map(
                    threat_level=unit_data['effectsCapability']
                ).upper()
            threats_to_add.append({
                'assetsThreatened': [
                    action['objective']
                ],
                'id': unit_data['id'],
                'name': unit_data['name'],
                'threatLevel': threat_capability,
                'purpose': 'Unknown',
                'motivation': 'Unknown',
                'intent': 'Unknown'
            })

    if "threats" not in system_data:
        system_data['threats'] = threats_to_add
    else:
        system_data["threats"] += threats_to_add

    return system_data


def add_site_group():
    return [
        {
            "id": "Sites",
            "name": "Sites",
            "description": "LayerType"
        }
    ]





# @todo Is this function still needed? It is not referenced anywhere
def combine_system_risk(system_data, asset_risk_scores):
    for asset in system_data['assets']:
        asset['riskScore'] = asset_risk_scores[asset['id']]['riskScore']
        asset['riskLabel'] = asset_risk_scores[asset['id']]['riskLabel']
        asset['criticalityScore'] = asset_risk_scores[asset['id']]['criticalityScore']
        asset['criticalityLabel'] = asset_risk_scores[asset['id']]['criticalityLabel']
    return system_data


# @todo Is this class still needed? It is not reference anywhere
class SystemAnalysis:
    def __init__(self):
        pass

    def save_system_data(self, system_data):
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        system_collection = client[os.environ.get('DB_NAME')]['system']
        system_collection.remove({"id": self.system_id})
        system_data.update({
            "_id": self.system_id
        })
        system_collection.insert(system_data)


# @todo Possible to combine functions number_of_vulnerabilities and number_of_threats
def number_of_vulnerabilities(asset_id, vulnerabilities):
    vuln_no = len(list(filter(lambda d: asset_id in d['assets'], vulnerabilities)))
    return vuln_no


def number_of_threats(asset_id, threats):
    threat_no = len(list(filter(lambda d: asset_id in d['assetsThreatened'], threats)))
    return threat_no


def asset_from_id(asset_id, assets, asset_type=False):
    for asset in assets:
        if asset_id == asset['id']:
            if asset_type:
                return asset['assetType']
            else:
                return asset


def remove_asset_by_id(asset_id, assets):
    for asset in assets:
        if asset_id == asset['id']:
            assets.remove(asset)
    return assets


def get_asset_threats(asset_id, threats):
    asset_threats = []
    for threat in threats:
        if asset_id in threat['assetsThreatened']:
            asset_threats.append(threat)
    return asset_threats


def get_leaf_nodes(course_of_action):
    leaf_nodes = []
    for task in course_of_action:
        parent_node = False
        for compare_task in course_of_action:
            if task['name'] in compare_task['dependencies']:
                parent_node = True
        if not parent_node:
            leaf_nodes.append(task['name'])
    return leaf_nodes


def get_all_parents(leaf_node, course_of_action):
    parent_tasks = []
    all_parents = [leaf_node]
    for i in range(len(course_of_action)):
        for task in course_of_action:
            if task['name'] in all_parents:
                if len(task['dependencies']) > 0:
                    all_parents = all_parents + task['dependencies']
                break
    all_parents = list(set(all_parents))
    for parent in all_parents:
        for task in course_of_action:
            if task['name'] == parent:
                parent_tasks.append(task)
    return parent_tasks


def get_branch_time(branch):
    branch_time = 0
    for task in branch:
        branch_time += task['calculatedTimeFrame']
    return branch_time


def exceeds_mission_time(course_of_action, dependencies):
    if dependencies:
        leaf_nodes = get_leaf_nodes(
            course_of_action=course_of_action
        )
        branch_times = []
        for leaf_node in leaf_nodes:
            all_parents = get_all_parents(
                leaf_node=leaf_node,
                course_of_action=course_of_action
            )
            branch_times.append(
                get_branch_time(
                    branch=all_parents
                )
            )
        coa_time = max(branch_times)
    else:
        coa_time = get_branch_time(
            branch=course_of_action
        )
    return coa_time
