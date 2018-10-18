import os

import pandas as pd
import pymongo as pm
import datetime as datetime

import random

import numpy.random as nprnd

from Risk import Risk


_author_ = 'Owen Sims (sims.owen@gmail.com)'


"""
A set of functions used to infer appropriate courses of action from the mission
network data, supplied by Risk Aware.
:Note:  Vulnerabilities --> Software --> Hardware --> Networks
        |---------- Actions ---------||-- Tasks --||--- Effects ---|
"""


class CoursesOfAction:
    def __init__(self, network_data, current_risk_scores):
        """
        Initiate the data to be passed on to functions within the class.
        """
        self.current_risk_scores = current_risk_scores
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['id', 'globalId', 'name', 'type', 'facility', 'summary'])
        self.arc_list_df = pd.DataFrame(network_data['edges'], columns = ['source', 'target'])


    def get_mission_objectives(self, mission_objective_label = 'Mission'):
        """
        A function used to gather all mission objectives. This will be given by
        the mission graph, supplied by Risk Aware.
        """
        objectives = []
        mission_objectives = self.node_list_df[self.node_list_df['type'] == mission_objective_label]['name'].values

        for i in range(len(mission_objectives)):
            objective_information = {}
            objective_information.update({
            'timestamp' : datetime.datetime.utcnow(),
            'missionObjective' : mission_objectives[i],
            'missionRiskTimeline' : self.get_mission_objective_risk(time_periods = 50)
            })

            objectives.append(objective_information)

        return objectives


    def get_mission_objective_risk(self, time_periods):
        """
        Collect the historical risk profile attached to the mission objective.
        """
        mission_objective_risk = []

        for i in range(time_periods):
            if i == 0:
                risk_score = max(self.current_risk_scores)
            else:
                risk_score = nprnd.randint(100, size = 1)[0]

            mission_objective_risk.append({
            'timestamp' : int(datetime.date.today().strftime("%s")) - (60 * 60 * 24 * i),
            'risk_score' : risk_score,
            'risk_label' : Risk(risk_score = risk_score).get_risk_label()
            })

        return mission_objective_risk


    def get_cyber_actions(self):
        """
        Derive a list of dictionaries regarding the potential cyber actions
        that a Defender can pursue. These actions are inherently tied to known
        software vulnerabilities.
        """
        self.node_list_df[self.node_list_df['type'] == 'SoftwareVulnerability']
        software_vulnerabilities_df = self.node_list_df[self.node_list_df['type'] == 'SoftwareVulnerability'][['id', 'name', 'summary']]

        software_vulnerabilities = []
        for i in software_vulnerabilities_df.index:
            vulnerability_id = software_vulnerabilities_df['id'][i]
            vulnerability_name = software_vulnerabilities_df['name'][i]
            vulnerability_summary = software_vulnerabilities_df['summary'][i]

            vulnerability_connections = self.arc_list_df[self.arc_list_df['target'] == vulnerability_id]

            vulnerable_softwares = []
            for j in vulnerability_connections['source']:
                source_index = self.node_list_df['id'].str.extract('(' + j + ')').dropna().index
                if self.node_list_df['type'][source_index].values[0] == 'Software':
                    source_name = self.node_list_df['name'][source_index]

                    software_info = {
                    'softwareId' : j,
                    'softwareName' : source_name.values[0],
                    'actionBenefit' : self.get_action_benefit(software_id = j)
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
        """
        Derive the benefit from patching a certain piece of software.
        """
        software_source_subset = self.arc_list_df[self.arc_list_df['source']==software_id]
        software_target_subset = self.arc_list_df[self.arc_list_df['target']==software_id]

        software_out_degree = len(software_source_subset)
        software_in_degree = len(software_target_subset)

        action_benefit = float(software_in_degree) / float(software_out_degree)

        return action_benefit


    def get_relative_action_priority(self, benefit, max_benefit, min_benefit):
        """
        Feature scaling for prioritising actions.
        """
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
        """
        Derive a list of dictionaries regarding the cyber actions and associated
        tasks on those actions.
        """
        software_vulnerabilities = self.get_cyber_actions()

        for i in range(len(software_vulnerabilities)):
            software_id = software_vulnerabilities[i]['softwareAffected'][0]['softwareId']
            hardware_id = list(self.arc_list_df[self.arc_list_df['target'] == software_id]['source'])

            software_sources = []
            networkNodes = []
            for j in hardware_id:
                if self.node_list_df[self.node_list_df['id'] == j]['type'].values[0] == 'Device':
                    hardware_globalId = self.node_list_df[self.node_list_df['id'] == j]['globalId']
                    hardware_id = self.node_list_df[self.node_list_df['id'] == j]['id']
                    hardware_name = self.node_list_df[self.node_list_df['id'] == j]['name']

                    networkNodes.append(hardware_globalId.values[0])

                    software_sources.append({
                    'hardwareGlobalId' :  hardware_globalId.values[0],
                    'hardwareName' : hardware_name.values[0],
                    'hardwareOrientId' : hardware_id.values[0]
                    })

            software_vulnerabilities[i].update({
            'hardwareAffected' : software_sources,
            'networkNodes' : networkNodes
            })

        return software_vulnerabilities


    def get_time_taken(self):
        """
        Derive the time taken for the course of action.
        """

        time_taken = {
        'averageTime' : 90,
        'standardDeviationTime' : 15
        }

        return time_taken


    def get_personnel_required(self):
        """
        Derive the time taken for the course of action.
        """

        personnel_required = [
        "2 security analysts"
        ]

        return personnel_required


    def get_expected_impact(self):
        """
        Derive the time taken for the course of action.
        """
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
        """
        Derive the mission effects attached to each: task --> action.
        """
        mission_objective = self.get_mission_objectives()
        software_vulnerabilities = self.get_cyber_tasks()
        for i in range(len(software_vulnerabilities)):
            software_vulnerabilities[i].update({
            'effect': 'Secure Enterprise Network',
            'missionObjective': mission_objective[0]['missionObjective'],
            'time_taken': self.get_time_taken(),
            'personnel_required': self.get_personnel_required(),
            'expectedImpact': self.get_expected_impact(),
            'active': 0,
            'staged': 0,
            'globalId': "coa" + str(i)
            })

        return software_vulnerabilities


    def get_post_all_courses_of_action(self, mongo_port = int(os.environ.get('DB_PORT')), mongo_collecton = "actions",
                                       mongo_database = os.environ.get('DB_NAME'), mongo_host = os.environ.get('DB_HOSTNAME')):
        courses_of_action = self.get_cyber_effects()
        mongo_connection = pm.MongoClient('mongodb://' + mongo_host + ':' + str(mongo_port) + '/')[mongo_database][mongo_collecton]
        mongo_connection.drop()
        mongo_result = mongo_connection.insert(courses_of_action)

        return mongo_result


class AssetCoursesOfAction:
    def __init__(self, asset_data):
        """
        Initiate the data to be passed on to functions within the class.
        """
        self.asset_list_df = pd.DataFrame(asset_data['assets'])
        self.vulnerability_list_df = pd.DataFrame(asset_data['vulnerabilities'])

    def get_mission_objectives(self):
        """
        A function used to gather all mission objectives. This will be given by
        the mission graph, supplied by Risk Aware.
        """
        objectives = []
        mission_objectives = ['Defend Power Station']
        for i in range(len(mission_objectives)):
            objective_information = {}
            objective_information.update({
                'timestamp': datetime.datetime.utcnow(),
                'missionObjective': mission_objectives[i],
                'missionRiskTimeline': self.get_mission_objective_risk(time_periods=50)
            })

            objectives.append(objective_information)
        return objectives

    def get_mission_objective_risk(self, time_periods):
        """
        Collect the historical risk profile attached to the mission objective.
        """
        mission_objective_risk = []
        for i in range(time_periods):
            risk_score = nprnd.randint(100, size=1)[0]
            mission_objective_risk.append({
                'timestamp': int(datetime.date.today().strftime("%s")) - (60 * 60 * 24 * i),
                'risk_score': risk_score,
                'risk_label': Risk(risk_score=risk_score).get_risk_label()
            })
        return mission_objective_risk

    def get_cyber_actions(self):
        """
        Derive a list of dictionaries regarding the potential cyber actions
        that a Defender can pursue. These actions are inherently tied to known
        software vulnerabilities.
        """
        asset_vulnerabilities = []
        for i in range(len(self.vulnerability_list_df)):
            vulnerability_id = self.vulnerability_list_df['vulnerabilityId'][i]
            vulnerability_name = self.vulnerability_list_df['name'][i]
            vulnerability_type = self.vulnerability_list_df['type'][i]

            vulnerable_assets = []
            for j in range(len(self.vulnerability_list_df['assets'][i])):
                asset_name = self.vulnerability_list_df['assets'][i][j]
                vulnerable_asset = self.asset_list_df[self.asset_list_df['assetId'] == asset_name]

                asset_info = {
                    'assetId': vulnerable_asset['assetId'].values[0],
                    'assetName': vulnerable_asset['name'].values[0],
                    'actionBenefit': random.random()
                }

                vulnerable_assets.append(asset_info)

            total_action_benefit = 0
            for j in range(len(vulnerable_assets)):
                total_action_benefit += vulnerable_assets[j]['actionBenefit']

            if vulnerability_type == 'Patch':
                desc_prefix = 'Employ a more routinised patching process for Asset '
            elif vulnerability_type == 'Physical':
                desc_prefix = 'Alocate more physical resources to Asset '

            asset_vulnerabilities.append({
                'vulnerability': vulnerability_name,
                'vulnerabilityId': vulnerability_id,
                'assets': vulnerable_assets,
                'actionClass': vulnerability_type,
                'actionType': 'Cyber',
                'benefit': total_action_benefit,
                'probabilityOfSuccess': 1,
                'description': desc_prefix + vulnerable_assets[0]['assetId']
            })

        action_benefits = []
        for i in range(len(asset_vulnerabilities)):
            action_benefits.append(asset_vulnerabilities[i]['benefit'])
        max_benefit = max(action_benefits)
        for i in range(len(asset_vulnerabilities)):
            priority_details = self.get_relative_action_priority(benefit = action_benefits[i], max_benefit = max_benefit, min_benefit = 0)
            asset_vulnerabilities[i].update({
            'priorityScore' : priority_details[0],
            'priorityLabel' : priority_details[1]
            })

        return asset_vulnerabilities

    def get_action_benefit(self):
        """
        Derive the benefit from patching a certain piece of software.
        !!!PLEASE DEVELOP FURTHER!!!
        """
        action_benefit = random.random()
        return action_benefit

    def get_relative_action_priority(self, benefit, max_benefit, min_benefit):
        """
        Feature scaling for prioritising actions.
        """
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
        return [normalized_benefit, relative_priority]

    def get_cyber_tasks(self):
        """
        Derive a list of dictionaries regarding the cyber actions and associated
        tasks on those actions.
        """
        asset_vulnerabilities = self.get_cyber_actions()

        for i in range(len(asset_vulnerabilities)):
            assets = []
            for j in range(len(asset_vulnerabilities[i]['assets'])):
                assets.append(asset_vulnerabilities[i]['assets'][j]['assetId'])

            asset_vulnerabilities[i]['assets'] = assets

        return asset_vulnerabilities

    def get_time_taken(self):
        """
        Derive the time taken for the course of action.
        """
        time_taken = {
            'averageTime': 90,
            'standardDeviationTime': 15
        }
        return time_taken

    def get_personnel_required(self):
        """
        Derive the time taken for the course of action.
        """
        personnel_required = [
            "2 security analysts"
        ]
        return personnel_required

    def get_expected_impact(self):
        """
        Derive the time taken for the course of action.
        """
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
        """
        Derive the mission effects attached to each: task --> action.
        """
        mission_objective = self.get_mission_objectives()
        asset_vulnerabilities = self.get_cyber_tasks()
        for i in range(len(asset_vulnerabilities)):
            asset_vulnerabilities[i].update({
                'effect': 'Secure Enterprise Network',
                'missionObjective': mission_objective[0]['missionObjective'],
                'timeTaken': self.get_time_taken(),
                'personnelRequired': self.get_personnel_required(),
                'expectedImpact': self.get_expected_impact(),
                'staged': 0,
                'completed': 0,
                'actionId': "COA" + str(i)
            })
        return asset_vulnerabilities

    def get_post_all_courses_of_action(self, mongo_port=int(os.environ.get('DB_PORT')), mongo_collecton='actions',
                                       mongo_database=os.environ.get('DB_NAME'), mongo_host=os.environ.get('DB_HOSTNAME')):
        actions = self.get_cyber_effects()
        mongo_connection = pm.MongoClient('mongodb://' + mongo_host + ':' + str(mongo_port) + '/')[mongo_database][mongo_collecton]
        mongo_connection.drop()
        mongo_result = mongo_connection.insert(actions)
        return mongo_result
