import os

import pymongo as pm


class NetworkAnalysis:
    def __init__(self, system_id):
        self.system_id = system_id

    def combine_network_risk(self, network_data, device_risk_scores):
        for node in network_data['nodes']:
            if 'globalId' in node.keys():
                if node['globalId'] in device_risk_scores.keys():
                    node['riskScore'] = device_risk_scores[node['globalId']]['riskScore']
                    node['riskLabel'] = device_risk_scores[node['globalId']]['riskLabel']
        return network_data

    def save_network_data(self, network_data):
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        system_collection = client[os.environ.get('DB_NAME')]['network']
        system_collection.remove({"system_id": self.system_id})
        network_data.update({
            "_id": self.system_id + '-NETWORK',
            "system_id" : self.system_id
        })
        system_collection.insert(network_data)