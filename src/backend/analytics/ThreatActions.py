import numpy as np
import pandas as pd


_author_ = 'Owen Sims (sims.owen@gmail.com)'


class ThreatActions:
    """
    Blah blah...
    """
    def __init__(self):
        """
        Initiate the data
        """
        self.node_list_df = pd.DataFrame(network_data['nodes'], columns = ['id', 'name', 'type', 'likelihood', 'sensitivity'])
        self.arc_list_df = pd.DataFrame(network_data['edges'], columns = ['id', 'source', 'target', 'type'])

    def threat_actions_vulnerabilities(self):
        """
        Derive the threat actions from the vulnerabilities within the network graph
        """
