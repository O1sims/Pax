import os

import pandas as pd
import pymongo as pm
import networkx as nx

_author_ = 'Owen Sims (sims.owen@gmail.com)'


class CurrentNetworkValue:
    """
    Derive the current network value for the Defender. Note that the risk attached
    to each node has to be calculated prior to running this.
    """
    def __init__(self):
        """
        Collect the node and edge data in order to run analysis.
        """
        mongo_client = pm.MongoClient(host = os.environ.get('DB_HOSTNAME'), port = int(os.environ.get('DB_PORT')))
        network_data_collection = mongo_client[os.environ.get('DB_NAME')]['network_data']
        network_data = network_data_collection.find()

        self.node_list_df = pd.DataFrame(network_data['nodes'])
        self.edge_list_df = pd.DataFrame(network_data['edges'])

        self.node_list_df = self.node_list_df[self.node_list_df['type'] == 'Device']

        for i in range(self.edge_list_df.shape[0]):
            if self.edge_list_df['source'][i] not in self.device_list_df['id'].values or self.edge_list_df['target'][i] not in self.device_list_df['id'].values:
                self.edge_list_df = self.edge_list_df.drop(i)


    def get_value_function(self):
        G_devices = nx.from_pandas_dataframe(self.edge_list_df, 'source', 'target')
        component_populations = [len(c) for c in sorted(nx.connected_components(G_devices), key = len, reverse = True)]

        # Allow function to be f(x) = x^2
        tau = 0
        for i in component_populations:
            tau += i**2


class CurrentPayoffValue:
    """
    Derive the payoff value for the Defender in persuing a specific course of action.
    This is maintained as a simple cost-benefit analysis.
    """
    def __init__(self, course_of_action_ids):
        """
        Collect course of action data from global IDs.
        """
        mongo_client = pm.MongoClient(host = os.environ.get('DB_HOSTNAME'), port = int(os.environ.get('DB_PORT')))
        coa_data_collection = mongo_client[os.environ.get('DB_NAME')]['courses_of_action_data']

        self.coa_data = []
        for i in course_of_action_ids:
            self.coa_data.append(coa_data_collection.find_one({"globalId" : i}))


    def get_payoff_values(self):
        """

        """
