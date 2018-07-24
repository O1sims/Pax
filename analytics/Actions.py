import os

import requests
import pymongo as pm

from analytics.SystemRisk import evaluate_system_risk


class SystemLevelActions:
    def __init__(self, system_data, system_id):
        self.system_data = system_data
        self.system_id = system_id
        self.initial_asset_risk = evaluate_system_risk(
            system_id=system_id,
            system_data=system_data
        )

    def get_actions(self):
        action_benefits = []
        asset_vulnerabilities = []
        for vulnerability in self.system_data['vulnerabilities']:
            new_asset_risk = self.recalculate_system_risk(
                system_id=self.system_id,
                system_data=self.system_data,
                vulnerability_id=vulnerability['id']
            )
            vulnerable_assets = {}
            benefit = 0
            for asset in vulnerability['assets']:
                vulnerable_assets.update({
                    asset: {
                        'initialRisk': self.initial_asset_risk[asset]['riskScore'],
                        'newRisk': new_asset_risk[asset]['riskScore']
                    }
                })
                benefit += self.initial_asset_risk[asset]['riskScore'] - new_asset_risk[asset]['riskScore']
            action_benefits.append(benefit)
            description = ""
            if vulnerability['type'] == 'Patch':
                description = 'Employ a more routinised patching process for Asset(s)'
            elif vulnerability['type'] == 'Physical':
                description = 'Allocate more physical resources to Asset(s)'
            asset_vulnerabilities.append({
                '_id': 'COA' + str(len(asset_vulnerabilities) + 1),
                'team': 'friendly',
                'system_id': self.system_id,
                'vulnerability': vulnerability['id'],
                'benefit': {
                    'assets': vulnerable_assets
                },
                'cost': self.get_action_cost(),
                'actionType': vulnerability['type'],
                'probabilityOfSuccess': 1,
                'description': description
            })
        max_benefit = max(action_benefits)
        for i in range(len(asset_vulnerabilities)):
            priority = self.get_relative_action_priority(
                benefit=action_benefits[i],
                max_benefit=max_benefit,
                min_benefit=0
            )
            asset_vulnerabilities[i].update({
                'priority': priority
            })
        return asset_vulnerabilities

    def get_action_cost(self):
        time_taken = 90
        units = {
            'Security analysts': 2
        }
        action_cost = {
            'timeTaken': time_taken,
            'personCost': units
        }
        return action_cost

    def get_relative_action_priority(self, benefit, max_benefit, min_benefit):
        normalized_benefit = 100 * (benefit - min_benefit) / (max_benefit - min_benefit)
        if normalized_benefit >= 87:
            relative_priority = 'Very High'
        elif normalized_benefit >= 75:
            relative_priority = 'High'
        elif normalized_benefit >= 62:
            relative_priority = 'Medium High'
        elif normalized_benefit >= 50:
            relative_priority = 'Medium'
        elif normalized_benefit >= 38:
            relative_priority = 'Medium Low'
        elif normalized_benefit >= 24:
            relative_priority = 'Low'
        else:
            relative_priority = 'Very Low'
        priority = {
            'score': normalized_benefit,
            'label': relative_priority
        }
        return priority

    def recalculate_system_risk(self, system_id, system_data, vulnerability_id):
        system_data['vulnerabilities'] = [v for v in system_data['vulnerabilities'] if v['id'] != vulnerability_id]
        asset_risk = evaluate_system_risk(
            system_id=system_id,
            system_data=system_data
        )
        return asset_risk

    def post_actions(self, action_data):
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        actions_collection = client[os.environ.get('DB_NAME')]['actions']
        actions_collection.drop()
        actions_collection.insert(action_data)

    def get_all_actions(self):
        actions = self.get_actions()
        self.post_actions(action_data=actions)


class ActionAnalysis:
    def __init__(self, action_data, system_id=None, system_data=None):
        self.actions = action_data
        self.system_id = system_id
        self.system_data = system_data

    @staticmethod
    def action_time_map():
        action_time = {
            "DESTROY": 5,
            "SECURE": 2,
            "UNDERSTAND": 2,
            "SEIZE": 1,
            "DISRUPT": 2,
            "DECEIVE": 1,
            "DENY": 1
        }
        return action_time

    def get_actor(self):
        actor_id = self.actions['actor']
        r = requests.get('http://' + os.environ.get('C2-REST') + 'entity/unit/' + actor_id)
        if r.status_code == 200:
            actor_data = r.json()
        else:
            r = requests.get('http://' + os.environ.get('C2-REST') + 'system/' + self.system_id + '/threats')
            threat_data = r.json()
            actor_data = [threat for threat in threat_data if threat['id'] == actor_id][0]
            actor_data.update({
                'affiliation': 'HOSTILE',
                'capabilityLevel': actor_data['threatLevel']
            })
        return actor_data

    def probability_of_success(self):
        """
        At the minute, the probability of an actions' success depends on the amount of time taken to achieve the effect.
        """
        action_time = self.action_time_map()
        for action in self.actions:
            if action_time[action['effect']] > action['timeFrame']:
                return 0
        return 1

