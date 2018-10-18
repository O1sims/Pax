import pandas as pd
import networkx as nx


class NetworkRisk:
    """
    This class ingests network data from Risk Aware and returns risk scores for all devices.
    Specifically, the risk scores are determined through a contagion centrality measure where the minimum path
    lengths are calculated between devices and known vulnerabilities.
    """
    def __init__(self, network_data):
        self.nodes = pd.DataFrame(network_data['nodes'], columns=['id', 'globalId', 'name', 'type'])
        self.devices = self.nodes[self.nodes['type'] == 'Device'].reset_index()
        self.vulnerabilities = self.nodes[self.nodes['type'] == 'SoftwareVulnerability'].reset_index()
        all_edges = pd.DataFrame(network_data['edges'], columns=['id', 'source', 'target', 'type'])
        self.edges = all_edges[all_edges['type'] != 'NetworkEdge']

    def get_risk_score(self, network, vulnerabilities, device_id, decay_rate=0.2):
        if vulnerabilities.size > 0:
            path_length = []
            for vulnerability_id in vulnerabilities['id']:
                path_length.append(len(nx.shortest_path(network, source=device_id, target=vulnerability_id)))
            min_path_length = min(path_length)
            risk_score = int(100 * (((min_path_length - 1) ** -1) ** decay_rate))
            return risk_score
        else:
            return 0

    def generate_risk_labels(self, risk_score):
        if risk_score >= 80:
            return 'Critical'
        elif risk_score >= 60:
            return 'High'
        elif risk_score >= 40:
            return 'Medium'
        elif risk_score >= 20:
            return 'Low'
        elif risk_score >= 0:
            return 'Very low'


    def evaluate_network_risk(self):
        G = nx.from_pandas_dataframe(df=self.edges, source='source', target='target')
        device_risk = {}
        for i in range(len(self.devices)):
            device_id = self.devices['id'][i]
            device_global_id = self.devices['globalId'][i]
            risk_score = self.get_risk_score(network=G, vulnerabilities=self.vulnerabilities, device_id=device_id)
            device_risk.update({
                device_global_id: {
                    'riskScore': risk_score,
                    'riskLabel': self.generate_risk_labels(risk_score=risk_score),
                }
            })
        return device_risk
