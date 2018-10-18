import os

import numpy as np
import pymongo as pm


_author_ = 'Owen Sims (sims.owen@gmail.com)'


def get_risk_appetite(system_id):
    client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
    ra_collection = client[os.environ.get('DB_NAME')]['risk_appetite']
    risk_appetite_data = ra_collection.find_one({"systemId": system_id})
    return risk_appetite_data


class RiskAppetiteAnalysis:
    """
    A class that generates a risk appetite score from data inserted in the
    Mongo collection `risk-appetite-data`.
    """
    def __init__(self, risk_appetite_data):
        """
        Initialise the class by collecting the risk appetite data and stores it
        as a dictionary.
        """
        self.riskAppetiteData = risk_appetite_data

    def generate_asset_weights(self):
        # How does the organization prioritize cyber assets over physical assets?
        physicalAssetQuantities = []
        physicalQuestions = [
        'riskAssetImportance',
        'riskQuantity',
        'currentSecurityRegimeImportance',
        'impactReplacingAssets',
        'impactDefenceEffort'
        ]

        # Find the relative weights attached to physical assets relative to cyber assets
        for i in range(len(physicalQuestions)):
            totalPhysical = float(self.riskAppetiteData[physicalQuestions[i]]['physicalAssets']) + float(self.riskAppetiteData[physicalQuestions[i]]['cyberAssets'])
            physicalAssetQuantities.append(float(self.riskAppetiteData[physicalQuestions[i]]['physicalAssets']) / totalPhysical)

        # Take some average of these weights
        physicalAssetWeight = np.mean(physicalAssetQuantities)

        # Return weights for physical and cyber assets
        return [physicalAssetWeight, 1 - physicalAssetWeight]

    def generate_risk_appetite_score(self):
        # Analyse mission risk
        missionRisk = (float(self.riskAppetiteData['riskAssetImportance']['cyberAssets']) + float(self.riskAppetiteData['riskAssetImportance']['physicalAssets'])) / 10

        # Analyse current security regime
        securityRegime = (float(self.riskAppetiteData['currentSecurityRegimeImportance']['cyberAssets']) + float(self.riskAppetiteData['currentSecurityRegimeImportance']['physicalAssets'])) / 10
        defenceEffort = (float(self.riskAppetiteData['impactDefenceEffort']['cyberAssets']) + float(self.riskAppetiteData['impactDefenceEffort']['physicalAssets'])) / 10

        riskAppetiteItems = [missionRisk, securityRegime, defenceEffort]
        riskAppetiteScore = np.mean(riskAppetiteItems) * 100

        return int(riskAppetiteScore)

    def generate_risk_appetite_label(self, riskAppetiteScore):
        """
        Bucket the risk appetite score to generate a relevant label
        """
        # Bucketing operation
        if riskAppetiteScore >= 87:
            riskAppetiteLabel = "Very risk loving"
        elif riskAppetiteScore >= 75:
            riskAppetiteLabel = "Risk loving"
        elif riskAppetiteScore >= 50:
            riskAppetiteLabel = "Risk neutral"
        elif riskAppetiteScore >= 25:
            riskAppetiteLabel = "Risk averse"
        else:
            riskAppetiteLabel = "Very risk averse"

        return riskAppetiteLabel
