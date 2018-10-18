from utils.Exceptions import BadValue

def calculate_asset_impact(asset):
    total_impact = 0

    for key, value in asset["impact"].items():

        if key != 'id':
            v = int(value)
            if v < 0 or v > 5:
                raise AssetImpactValueOutOfRange(key, v)

            total_impact += v

    impact_score = int(100 * (float(total_impact)/15.0))

    return impact_score


def calculate_asset_criticality(asset):

    sensitivity = 0.8

    if "sensitivity" in asset:

        sen = int(asset["sensitivity"])

        if sen < 0 or sen > 5:
            raise AssetImpactValueOutOfRange("sensitivity", sen)

        sensitivity = float(asset["sensitivity"]) / 5.0

    impact_score = calculate_asset_impact(asset)
    criticality_score = int(sensitivity * impact_score)

    return criticality_score


def highest_criticality_asset(assets):
    max_criticality = 0
    for asset in assets:
        criticality = calculate_asset_criticality(asset=asset)
        if criticality > max_criticality:
            max_criticality = criticality
            highest_criticality_asset = asset
    return highest_criticality_asset



class AssetImpactValueOutOfRange(BadValue):

    def __init__(self, field, value):

        message = "The field {} with value of {} is out of range".format(field, value)

        super(AssetImpactValueOutOfRange, self).__init__(message)
