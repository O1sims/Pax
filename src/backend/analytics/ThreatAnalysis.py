import numpy as np
import pandas as pd


_author_ = 'Owen Sims (sims.owen@gmail.com)'


class CVIThreats:
    def __init__(self, cvi_data):
        self.asset_list_df = pd.DataFrame(cvi_data['assets'])
        self.threat_list_df = pd.DataFrame(cvi_data['threats'])


    def get_asset_threats(self):
        threats = dict()
        for i in range(len(self.asset_list_df)):
            threats[i] = list()
            for j in range(len(self.threat_list_df)):
                if self.asset_list_df['assetId'][i] in self.threat_list_df['assetsThreatened'][j]:
                    a = self.threat_list_df.iloc[[j]].to_dict(orient = 'dict')
                    d = dict()
                    for k in list(self.threat_list_df):
                        if k != 'assetsThreatened':
                            d.update({
                            k : a[k][j]
                            })

                    threats[i].append(d)

        return threats
