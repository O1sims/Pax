import os

import pymongo as pm
from bson.objectid import ObjectId

import datetime as datetime
import numpy.random as nprnd

from analytics.NetworkStatistics import TopologicalRisk
from analytics.SystemRisk import SystemRisk

from utils.Exceptions import BadValue


_author_ = 'Owen Sims (sims.owen@gmail.com)'


"""
A set of functions used to measure a client's risk appetite given a set of
responses to a risk appetite questionnaire.
"""


class Risk:
    """
    @todo As the risk score is only used by the get_risk_label function the function could be made standalone
    """
    def __init__(self, risk_score):
        self.risk_score = risk_score

    def get_risk_label(self):
        """
        Bucket a risk score (between 0 and 100) to generate the relevant risk
        label.
        """
        if self.risk_score < 0 or self.risk_score > 100:
            raise RiskScoreOutRange(self.risk_score)

        if self.risk_score >= 80:
            riskLabel = "Critical"
        elif self.risk_score >= 60:
            riskLabel = "High"
        elif self.risk_score >= 40:
            riskLabel = "Medium"
        else:
            riskLabel = "Low"

        return riskLabel

class RiskScoreOutRange(BadValue):

    def __init__(self, score):
        message = "Risk score {} is out of range of 0 >= x >= 100".format(score)

        super(RiskScoreOutRange, self).__init__(message)


class CalculateAssetRisk:
    def __init__(self):
        self.data = {}
        fields = [
            'assets',
            'vulnerabilities',
            'threats',
            'impacts'
        ]
        for field in fields:
            self.client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
            db_collection = self.client[os.environ.get('DB_NAME')][field]
            self.data.update({
                field: list(db_collection.find())
            })

    def asset_risk(self):
        self.data['threats'] = list(filter(lambda d: d['exists'] in [1], self.data['threats']))
        self.data['vulnerabilities'] = list(filter(lambda d: d['exists'] in [1], self.data['vulnerabilities']))

        for threat in self.data['threats']:
            threat['level'] = self.threat_level(threat['threatLevel'])
            threat['alphaLevel'] = float(threat['level']) / float(5)
        vulnerability_no = []
        threat_alpha = []
        impact_value = []
        for asset in self.data['assets']:
            value = 0
            asset_impacts = list(filter(lambda d: d['assetId'] in [asset['assetId']], self.data['impacts']))
            cia = ['confidentiality', 'integrity', 'availability']
            for characteristic in cia:
                value += int(asset_impacts[0][characteristic])
            impact_value.append(value)
            asset_vulnerabilities = list(
                filter(lambda d: asset['assetId'] in d['assets'], self.data['vulnerabilities']))
            vulnerability_no.append(len(asset_vulnerabilities))
            asset_threats = list(filter(lambda d: asset['assetId'] in d['assetsThreatened'], self.data['threats']))
            total_threat_alpha = 0
            for threat in asset_threats:
                total_threat_alpha += threat['alphaLevel']
            threat_alpha.append(total_threat_alpha)
        risk_scores = []
        for i in range(len(self.data['assets'])):
            interaction = vulnerability_no[i] * threat_alpha[i]
            if interaction > 0:
                risk_score = 100 * threat_alpha[i]
                risk_scores.append(risk_score)
            else:
                risk_scores.append(0)
        self.update_asset_details(risk_scores=risk_scores, asset_data=self.data['assets'])

        return {
            'risk_scores': risk_scores,
            'assets': self.data['assets']
        }

    def risk_label(self, risk_score):
        if risk_score >= 80:
            return 'Critical'
        elif risk_score >= 70:
            return 'High'
        elif risk_score >= 50:
            return 'Medium'
        elif risk_score >= 20:
            return 'Low'
        elif risk_score >= 0:
            return 'Very low'

    def threat_level(self, threat_label):
        if threat_label == 'Negligible':
            return 0
        elif threat_label == 'Low':
            return 1
        elif threat_label == 'Moderate':
            return 2
        elif threat_label == 'Substantial':
            return 3
        elif threat_label == 'Severe':
            return 4
        elif threat_label == 'Critical':
            return 5
        else:
            return 0

    def update_asset_details(self, risk_scores, asset_data):
        """
        Update assets with details on their risk scores and labels
        """
        asset_collection = self.client[os.environ.get('DB_NAME')]['assets']
        for i in range(len(asset_data)):
            historical_risk_scores = self.generate_historical_asset_risk_scores(time_periods=50)
            asset_collection.update_one(filter={'assetId': asset_data[i]['assetId']},
                                        update={'$set': {'riskScore': risk_scores[i],
                                                         'riskLabel': self.risk_label(risk_score=risk_scores[i]),
                                                         'historicalRiskScores': historical_risk_scores}})

    def generate_historical_asset_risk_scores(self, time_periods):
        """
        Generate risk scores and attach them to all assets.
        """
        historical_risk_scores = []
        for j in range(time_periods):
            risk_score = nprnd.randint(100, size = 1)[0]

            historical_risk_scores.append({
                'timestamp': int(datetime.date.today().strftime("%s")) - (60 * 60 * 24 * (j)),
                'risk_score': risk_score
            })

        return historical_risk_scores


class RecalculateRisk:
    def __init__(self, id, active_status, globalId):
        """
        Initialise the `RecalculateRisk` function
        """
        self.id = id
        self.globalId = globalId
        self.active_status = active_status
        self.mongo_client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port = int(os.environ.get('DB_PORT')))
        self.vulnerability_id = self.get_vulnerability_id(id = id)
        self.toggle_quantum_state()

    def preliminary_risk_result(self):
        risk_results = TopologicalRisk(from_mongo=True).asset_vulnerability_risk()
        return risk_results[self.globalId]

    def get_vulnerability_id(self, id):
        coa_data_collection = self.mongo_client[os.environ.get('DB_NAME')]['courses_of_action_data']
        vulnerability_id = coa_data_collection.find_one({'_id' : ObjectId(id)}, {'_id' : 0, 'vulnerabilityId' : 1})['vulnerabilityId']

        if self.active_status == '1':
            coa_data_collection.update_one({'_id': ObjectId(id)}, {'$set': {'staged': 1}})
        elif self.active_status == '0':
            coa_data_collection.update_one({'_id': ObjectId(id)}, {'$set': {'staged': 0}})

        return vulnerability_id

    def toggle_quantum_state(self):
        """
        Toggle the quantum state of the vulnerability node.
        """
        node_data_collection = self.mongo_client[os.environ.get('DB_NAME')]['node_data']
        if self.active_status == '1':
            node_data_collection.update_one({'id': self.vulnerability_id}, {'$set': {'quantumState': 1}}, upsert=False)
        elif self.active_status == '0':
            node_data_collection.update_one({'id': self.vulnerability_id}, {'$set': {'quantumState': 0}}, upsert=False)

    def recalculate_risk_from_change_in_coa(self):
        """
        Given a change in CoA, recalculate each nodes risk value and update
        Mongo.
        Process:
            (1) Take in nodes affected by the change in the CoAs status;
            (2) Collect nodes risk data from the `node_data` collection;
            (3) Provide new risk scores for nodes; and
            (4) Update the risk scores in the collection.
        """
        node_data_collection = self.mongo_client[os.environ.get('DB_NAME')]['node_data']
        for node in self.nodes_affected:
            current_risk_score = node_data_collection.find_one({'globalId': node}, {'_id': 0, 'currentRiskScore': 1})['currentRiskScore']
            # Let's keep it at 25 for now... though we will need to send this
            #  data elsewhere to run full analysis
            risk_differential = 25
            if self.active_status == 1:
                new_risk_score = current_risk_score - risk_differential
            elif self.active_status == 0:
                new_risk_score = current_risk_score + risk_differential
            node_data_collection.update_one({'globalId': node}, {'$set': {'currentRiskScore' : current_risk_score}})


class CalculateMissionRisk:
    def __init__(self):
        self.client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        assets_collection = self.client[os.environ.get('DB_NAME')]['assets']
        self.assets = list(assets_collection.find())

    def mission_risk(self):
        risk_scores = self.collect_risk_scores()
        mission_risk_score = self.derive_mission_risk(risk_scores=risk_scores)
        mission_risk_label = self.mission_risk_label(mission_risk_score=mission_risk_score)
        mission_risk = {
            'score': mission_risk_score,
            'label': mission_risk_label
        }
        self.post_mission_risk(mission_risk=mission_risk, mission_id='M0')

    def derive_mission_risk(self, risk_scores):
        mission_risk_score = reduce(lambda x, y: x + y, risk_scores) / len(risk_scores)
        return mission_risk_score

    def collect_risk_scores(self):
        risk_scores = []
        for asset in self.assets:
            risk_scores.append(asset['riskScore'])
        return risk_scores

    def mission_risk_label(self, mission_risk_score):
        if mission_risk_score >= 80:
            return 'Critical'
        elif mission_risk_score >= 70:
            return 'High'
        elif mission_risk_score >= 50:
            return 'Medium'
        elif mission_risk_score >= 20:
            return 'Low'
        elif mission_risk_score >= 0:
            return 'Very low'

    def post_mission_risk(self, mission_risk, mission_id):
        missions_collection = self.client[os.environ.get('DB_NAME')]['missions']
        missions_collection.update_one(filter={'missionId': mission_id}, update={'$set': {'missionRisk': mission_risk}})


class RiskTableAnalysis:
    def __init__(self, system_data, asset_risk):
        self.system_data = system_data
        self.asset_risk = asset_risk

    def generate_risk_summary(self, asset, vulnerabilities, threats):
        if len(vulnerabilities) > 1:
            v = "These vulnerabilities are"
            v_plural = "number of vulnerabilities, including: "
            vulnerabilities_string = ""
            for i in range(len(vulnerabilities)):
                vulnerability_description = vulnerabilities[i]['description'].lower()
                if i == 0:
                    additional_string = vulnerability_description
                elif i == len(vulnerabilities) - 1:
                    additional_string = " and " + vulnerability_description
                else:
                    additional_string = ", " + vulnerability_description
                vulnerabilities_string = vulnerabilities_string + additional_string
        else:
            v = "This vulnerability is"
            v_plural = "vulnerability which is that "
            vulnerabilities_string = vulnerabilities[0]['description'].lower()
        if threats is None:
            return "The " + asset['name'] + " has a " + v_plural + vulnerabilities_string + " "
        if len(threats) > 1:
            plural_threats = "threats"
            threat_string = ""
            for i in range(len(threats)):
                threat_name = threats[i]['name'] + ' (' + threats[i]['threatLevel'].capitalize() + ')'
                if i == 0:
                    additional_string = threat_name
                elif i == len(threats) - 1:
                    additional_string = " and " + threat_name
                else:
                    additional_string = ", " + threat_name
                threat_string = threat_string + additional_string
        else:
            plural_threats = "threat"
            threat_string = threats[0]['name'] + ' (' + threats[0]['threatLevel'].capitalize() + ')'
        summary = "The " + asset['name'] + " has a " + v_plural + vulnerabilities_string + " "
        summary = summary + v + " being subjected to the " + plural_threats + ": " + threat_string + "."
        return summary

    def generate_row(self, row_number, asset, vulnerabilities, threats, risk_level, vulnerability_only=False):
        risk_summary = self.generate_risk_summary(asset=asset, vulnerabilities=vulnerabilities, threats=threats)
        row = {
            'riskID': 'R' + str(row_number),
            'summary': risk_summary,
            'untreatedRiskLevel': risk_level['riskLabel'],
            'treatedRiskLevel': SystemRisk(system_data=self.system_data).if_asset_is_treated(asset=asset)
        }
        return row

    def generate_risk_table(self):
        number = 0
        risk_table = []
        for asset in self.system_data['assets']:
            vulnerabilities = list(filter(lambda d: asset['id'] in d['assets'], self.system_data['vulnerabilities']))
            threats = list(filter(lambda d: asset['id'] in d['assetsThreatened'], self.system_data['threats']))
            if len(vulnerabilities) > 0 and len(threats) > 0:
                number += 1
                row = self.generate_row(row_number=number, asset=asset, vulnerabilities=vulnerabilities, threats=threats, risk_level=self.asset_risk[asset['id']])
                risk_table.append(row)
            if len(vulnerabilities) > 0 and len(threats) == 0:
                number += 1
                row = self.generate_row(row_number=number, asset=asset, vulnerabilities=vulnerabilities, threats=None, risk_level=self.asset_risk[asset['id']], vulnerability_only=True)
                risk_table.append(row)
        return risk_table
