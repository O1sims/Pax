import os

import pandas as pd
import pymongo as pm
import random as random


class NetworkVulnerabilities:
    def __init__(self, vulnerability_data, device_data, edge_data, vulnerabilityType='Cyber'):
        self.vulnerability_df = pd.DataFrame(vulnerability_data, columns=['name', 'summary', 'id'])
        self.vulnerability_df.rename(columns={'summary': 'description'}, inplace=True)
        self.device_df = pd.DataFrame(device_data, columns=['id', 'globalId', 'facility'])
        self.edge_df = pd.DataFrame(edge_data)
        self.vulnerability_list = []
        for i in range(len(self.vulnerability_df)):
            self.vulnerability_list.append(self.vulnerability_df.iloc[i].to_dict())
            id = str(self.vulnerability_df['id'][i])
            assets_affected = []
            software_affected = list(self.edge_df[self.edge_df['target'] == id]['source'])
            for software in software_affected:
                devices_affected = list(self.edge_df[self.edge_df['target'] == software]['source'])
                for device in devices_affected:
                    device_facility = list(self.device_df[self.device_df['id'] == device]['facility'])
                    if device_facility != []:
                        assets_affected.append(device_facility)
            assets = list(set(reduce(lambda x, y: x + y, assets_affected, [])))
            self.vulnerability_list[i].update({
                'assets': assets,
                'origin': 'TVA',
                'exists': 1,
                'type': vulnerabilityType,
                'vulnerabilityId': 'V' + str(i + 10)
            })

    def post_network_vulnerabilities(self):
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        vulnerability_collection = client[os.environ.get('DB_NAME')]['vulnerabilities']
        vulnerability_collection.insert(self.vulnerability_list)


class NetworkVulnerabilityActions:
    def __init__(self, network_data):
        """
        Initiate the data to be passed on to functions within the class.
        """
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['id', 'name', 'facility', 'type', 'globalId'])
        self.arc_list_df = pd.DataFrame(network_data['edges'], columns = ['source', 'target'])

    def get_cyber_actions(self):
        """
        Derive a list of dictionaries regarding the potential cyber actions
        that a Defender can pursue. These actions are inherently tied to known
        software vulnerabilities.
        """
        software_vulnerabilities_df = self.node_list_df[self.node_list_df['type'] == 'SoftwareVulnerability'][['id', 'name', 'facility', 'type']]
        software_vulnerabilities = []
        for i in software_vulnerabilities_df.index:
            vulnerability_id = software_vulnerabilities_df['id'][i]
            vulnerability_name = software_vulnerabilities_df['name'][i]
            vulnerability_connections = self.arc_list_df[self.arc_list_df['target'] == vulnerability_id]
            vulnerable_softwares = []
            for j in vulnerability_connections['source']:
                source_index = self.node_list_df['id'].str.extract('(' + j + ')').dropna().index
                if self.node_list_df['type'][source_index].values[0] == 'Software':
                    source_name = self.node_list_df['name'][source_index]

                    software_info = {
                    'softwareId': j,
                    'softwareName': source_name.values[0],
                    'actionBenefit': self.get_action_benefit(software_id = j)
                    }

                    vulnerable_softwares.append(software_info)
            total_action_benefit = 0
            for j in range(len(vulnerable_softwares)):
                total_action_benefit += vulnerable_softwares[j]['actionBenefit']
            software_vulnerabilities.append({
                'vulnerability': vulnerability_name,
                'vulnerabilityId': vulnerability_id,
                'softwareAffected': vulnerable_softwares,
                'actionClass': 'Patch',
                'actionType': 'Cyber',
                'benefit': total_action_benefit,
                'probabilityOfSuccess': 1,
                'description': 'Patch vulnerability ' + vulnerability_name + ' attached to ' + vulnerable_softwares[0]['softwareName']
            })
        action_benefits = []
        for i in range(len(software_vulnerabilities)):
            action_benefits.append(software_vulnerabilities[i]['benefit'])
        max_benefit = max(action_benefits)
        for i in range(len(software_vulnerabilities)):
            priority_details = self.get_relative_action_priority(benefit=action_benefits[i], max_benefit=max_benefit, min_benefit=0)
            software_vulnerabilities[i].update({
                'priorityScore': priority_details[0],
                'priorityLabel': priority_details[1]
            })
        return software_vulnerabilities

    def get_action_benefit(self, software_id):
        software_source_subset = self.arc_list_df[self.arc_list_df['source']==software_id]
        software_target_subset = self.arc_list_df[self.arc_list_df['target']==software_id]
        software_out_degree = len(software_source_subset)
        software_in_degree = len(software_target_subset)
        action_benefit = float(software_in_degree) / float(software_out_degree)
        return action_benefit

    def get_relative_action_priority(self, benefit, max_benefit, min_benefit):
        normalized_benefit = 100 * (benefit-min_benefit)/(max_benefit-min_benefit)
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
        return [normalized_benefit, relative_priority]

    def get_cyber_tasks(self):
        software_vulnerabilities = self.get_cyber_actions()
        for i in range(len(software_vulnerabilities)):
            software_id = software_vulnerabilities[i]['softwareAffected'][0]['softwareId']
            hardware_id = list(self.arc_list_df[self.arc_list_df['target'] == software_id]['source'])
            assets_associated = []
            devices_associated = []
            for j in hardware_id:
                if self.node_list_df[self.node_list_df['id'] == j]['type'].values[0] == 'Device':
                    devices = self.node_list_df[self.node_list_df['id'] == j]['globalId'].values[0]
                    assets = list(self.node_list_df[self.node_list_df['id'] == j]['facility'])
                    assets_associated.append(assets)
                    devices_associated.append(devices)
            software_vulnerabilities[i].update({
                'assets': list(set(reduce(lambda x, y: x + y, assets_associated, []))),
                'devices': devices_associated
            })
        return software_vulnerabilities

    def get_time_taken(self):
        time_taken = {
            'averageTime': 90,
            'standardDeviationTime': 15
        }

        return time_taken

    def get_personnel_required(self):
        personnel_required = [
        "2 security analysts"
        ]

        return personnel_required

    def get_expected_impact(self):
        normalizer = 0
        expectedImpact = []
        numberOfPayoffs = random.randint(1, 5)
        for i in range(numberOfPayoffs):
            payoff = {
            'impactChange': random.randint(1, 5),
            'likelihood': float(random.randint(1,9)) / float(10)
            }
            normalizer += payoff['likelihood']
            expectedImpact.append(payoff)
        for i in range(numberOfPayoffs):
            expectedImpact[i]['likelihood'] = float(expectedImpact[i]['likelihood']) / float(normalizer)
        return expectedImpact

    def get_cyber_effects(self):
        software_vulnerabilities = self.get_cyber_tasks()
        for i in range(len(software_vulnerabilities)):
            software_vulnerabilities[i].update({
                'effect': 'Secure Enterprise Network',
                'missionObjective': 'Secure Power Plant',
                'timeTaken': self.get_time_taken(),
                'personnelRequired': self.get_personnel_required(),
                'expectedImpact': self.get_expected_impact(),
                'staged': 0
            })
        return software_vulnerabilities

    def post_actions(self):
        actions = self.get_cyber_effects()
        self.client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        self.action_collection = self.client[os.environ.get('DB_NAME')]['actions']
        actions = self.generate_action_id(action_list=actions, action_count=self.action_collection.count())
        self.action_collection.insert(actions)

    def generate_action_id(self, action_list, action_count):
        for i in range(len(action_list)):
            action_list[i].update({
                'actionId': 'COA' + str((i + 1))
            })
        return action_list
