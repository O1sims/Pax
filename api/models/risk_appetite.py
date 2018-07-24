from mongoengine import *


class RiskAppetite(Document):
    # Mission ID
    missionId = StringField(required=False)

    # Personal information
    personalFirstName = StringField(required=False)
    personalMiddleName = StringField(required=False)
    personalLastName = StringField(required=False)
    personalRank = StringField(required=False)
    personalLocation = StringField(required=False)

    # Mission information
    missionPurpose = StringField(required=False)
    missionSuccess = StringField(required=False)
    missionFailure = StringField(required=False)
    currentThreatAndRisk = ListField(required=False)

    # Risk information
    riskAssetImportance = DictField(required=False)
    riskRequiredSecurity = DictField(required=False)
    riskQuantity = DictField(required=False)
    riskFrequency = IntField(min_value=1, max_value=5, required=False)

    # Current security information
    currentSecurityRegime = StringField(required=False)
    currentSecurityRegimeResources = StringField(required=False)
    currentSecurityRegimeImportance = DictField(required=False)
    currentSecurityRegimePerformance = IntField(min_value=1, max_value=5, required=False)
    currentSecurityRegimeHomeComparison = IntField(min_value=1, max_value=5, required=False)

    # Vulnerability information
    vulnerabilityExposure = StringField(required=False)
    vulnerabilityIntelFrequency = IntField(min_value=1, max_value=5, required=False)
    vulnerabilityPatchingRegime = IntField(min_value=1, max_value=2, required=False)
    vulnerabilityPatchingRegimeFrequency = IntField(min_value=1, max_value=5, required=False)
    vulnerabilityPrioritisePatching = IntField(min_value=1, max_value=5, required=False)
    vulnerabilityAddedResources = IntField(min_value=1, max_value=2, required=False)
    vulnerabilityHypothetical = IntField(min_value=1, max_value=5, required=False)
    vulnerabilityHypotheticalSub = IntField(min_value=1, max_value=5, required=False)

    # Impact information
    impactWillingnessToLoseAssets = IntField(min_value=1, max_value=5, required=False)
    impactHowManyAssetsToLose = IntField(min_value=1, max_value=5, required=False)
    impactReplacingAssets = DictField(required=False)
    impactDefenceEffort = DictField(required=False)

    # Threat information
    threatLevel = IntField(min_value=1, max_value=5, required=False)
    threatFrequency = IntField(min_value=1, max_value=5, required=False)
    threatFriendlyForces = IntField(min_value=1, max_value=2, required=False)
    threatTolerance = IntField(min_value=1, max_value=5, required=False)
    threatResponse = DictField(required=False)
    riskAppetiteScore = IntField(min_value=0, max_value=100, required=False)
    riskAppetiteLabel = StringField(required=False)
