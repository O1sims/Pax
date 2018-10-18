import os

import pandas as pd
import pymongo as pm
import datetime as datetime

import numpy.random as nprnd

from Risk import Risk


_author_ = 'Owen Sims (sims.owen@gmail.com)'


"""
A set of functions used to infer information about the mission from the mission
network data, supplied by Risk Aware.
:Note:  Vulnerabilities --> Software --> Hardware --> Networks
        |---------- Actions ---------||-- Tasks --||--- Effects ---|
"""


class MissionAnalysis:
    def __init__(self, network_data, current_risk_scores):
        """
        Initiate the data to be passed on to functions within the class.
        """
        self.current_risk_scores = current_risk_scores
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns=['id', 'name', 'type', 'facility', 'summary'])
        self.arc_list_df = pd.DataFrame(network_data['edges'], columns=['source', 'target'])

    def get_mission_objectives(self, mission_objective_label='Vignette'):
        """
        A function used to gather all mission objectives. This will be given by
        the mission graph, supplied by Risk Aware.
        """
        objectives = []
        mission_objectives = self.node_list_df[self.node_list_df['type'] == mission_objective_label]['name'].values
        for i in range(len(mission_objectives)):
            objective_information = {}
            objective_information.update({
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
            if i == 0:
                risk_score = max(self.current_risk_scores)
            else:
                risk_score = nprnd.randint(100, size=1)[0]
            mission_objective_risk.append({
                'timestamp': int(datetime.date.today().strftime("%s")) - (60 * 60 * 24 * i),
                'risk_score': risk_score,
                'risk_label': Risk(risk_score = risk_score).get_risk_label()
            })
        return mission_objective_risk

    def get_all_mission_data(self):
        mission_data = self.get_mission_objectives()
        return mission_data

    def get_post_all_mission_data(self, mongo_port=int(os.environ.get('DB_PORT')), mongo_collecton="missions",
                                  mongo_database=os.environ.get('DB_NAME'), mongo_host=os.environ.get('DB_HOSTNAME')):
        mission_data = self.get_all_mission_data()

        mongo_connection = pm.MongoClient('mongodb://' + mongo_host + ':' + str(mongo_port) + '/')[mongo_database][mongo_collecton]
        mongo_connection.drop()
        mission_data[0].update({
            'missionId': 'M' + str(mongo_connection.count())
        })
        mongo_result = mongo_connection.insert(mission_data)

        return mongo_result
