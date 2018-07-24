from rest_framework import serializers


class HostileResponeDetails(serializers.Serializer):
    description = serializers.CharField(required=False)
    probabilityOfSuccessScore = serializers.IntegerField(min_value=0, required=False)
    effect = serializers.CharField(required=False)
    actions = serializers.ListField(child=serializers.CharField(), required=False)
    riskScoreAfter = serializers.IntegerField(min_value=0, required=False)
    impactLabel = serializers.CharField(required=False)
    actor = serializers.CharField(required=False)
    impactScore = serializers.IntegerField(min_value=0, required=False)
    objective = serializers.CharField(required=False)
    probabilityOfSuccessScoreLabel = serializers.CharField(required=False)
    riskLabelAfter = serializers.CharField(required=False)


class HostileResponseAction(serializers.Serializer):
    mostDangerous = serializers.ListField(child=HostileResponeDetails(), required=False)
    mostLikely = serializers.ListField(child=HostileResponeDetails(), required=False)


class AssetRisk(serializers.Serializer):
    riskLabel = serializers.CharField(required=False)
    impactScore = serializers.IntegerField(min_value=0, required=False)
    riskSummary = serializers.CharField(required=False)
    criticalityLabel = serializers.CharField(required=False)
    likelihoodScore = serializers.IntegerField(min_value=0, required=False)
    criticalityScore = serializers.IntegerField(min_value=0, required=False)
    likelihoodLabel = serializers.CharField(required=False)
    riskScore = serializers.IntegerField(min_value=0, required=False)
    impactLabel = serializers.CharField(required=False)


class AssetRiskBlock(serializers.Serializer):
    hostileResponses = HostileResponseAction(required=False)
    risks = serializers.ListField(child=AssetRisk(), required=False)


class AssetRiskResult(serializers.Serializer):
    assetLabel = AssetRiskBlock(required=False, many=True)
