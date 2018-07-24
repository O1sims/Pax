from rest_framework import serializers


ASSET_TYPES = (
    "physical", "cyber", "unit"
)

THREAT_LEVELS = (
    "NONE", "LOW", "MODERATE", "SEVERE"
)

THREAT_TYPES = (
    "hacker", "terrorist"
)


class VulnerabilitiesModel(serializers.Serializer):
    id = serializers.CharField(required=True)
    assets = serializers.ListField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    type = serializers.ChoiceField(
        choices=ASSET_TYPES,
        required=True)


class ThreatsModel(serializers.Serializer):
    id = serializers.CharField(required=True)
    assetsThreatened = serializers.ListField(required=True)
    name = serializers.CharField(required=True)
    motivation = serializers.CharField(required=True)
    purpose = serializers.CharField(required=True)
    intent = serializers.CharField(required=True)
    threatLevel = serializers.ChoiceField(
        choices=THREAT_LEVELS,
        required=True)
    type = serializers.ChoiceField(
        choices=THREAT_TYPES,
        required=False)


class ImpactModel(serializers.Serializer):
    id = serializers.CharField(required=True)
    confidentiality = serializers.IntegerField(
        min_value=1, max_value=5, required=True)
    integrity = serializers.IntegerField(
        min_value=1, max_value=5, required=True)
    availability = serializers.IntegerField(
        min_value=1, max_value=5, required=True)


class AssetsModel(serializers.Serializer):
    id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    assetType = serializers.ChoiceField(
        choices=ASSET_TYPES,
        required=True)
    group = serializers.CharField(required=True)
    function = serializers.CharField(required=True)
    impact = ImpactModel(many=False, required=True)
    sensitivity = serializers.IntegerField(required=True)


class GroupsModel(serializers.Serializer):
    id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)


class FunctionsModel(serializers.Serializer):
    id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    reference = serializers.CharField(required=False)


class CVISystemModel(serializers.Serializer):
    id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    groups = GroupsModel(many=True, required=True)
    functions = FunctionsModel(many=True, required=True)
    assets = AssetsModel(many=True, required=True)
    threats = ThreatsModel(many=True, required=True)
    vulnerabilities = VulnerabilitiesModel(many=True, required=True)
