class CVIImpacts:
    def __init__(self, asset_data):
        self.asset_data = asset_data


    def combine_assets_and_impacts(self):
        for i in range(len(self.asset_data['assets'])):
            asset_name = self.asset_data['assets'][i]['name']
            for j in range(len(self.asset_data['impacts'])):
                if asset_name == self.asset_data['impacts'][j]['assetName']:
                    self.asset_data['assets'][i]['impacts'] = self.asset_data['impacts'][j]

        return self.asset_data
