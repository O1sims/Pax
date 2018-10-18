from rest_framework import serializers


EFFECTS_LIST = (
    "DESTROY", "DECEIVE", "DENY", "SEIZE",
    "UNDERSTAND", "SECURE", "DISRUPT"
)

EFFECT_TYPES = (
    "offensive", "defensive"
)


class HostileResponsesModel(serializers.Serializer):
    mostDangerous = serializers.ChoiceField(
        choices=EFFECTS_LIST,
        required=True)
    mostLikely = serializers.ChoiceField(
        choices=EFFECTS_LIST,
        required=True)


class EffectPropertiesModel(serializers.Serializer):
    actor = HostileResponsesModel(required=True)
    cyber = HostileResponsesModel(required=True)
    physical = HostileResponsesModel(required=True)


class EffectsModel(serializers.Serializer):
    description = serializers.CharField(required=True)
    effect = serializers.ChoiceField(
        choices=EFFECTS_LIST,
        required=True)
    type = serializers.ChoiceField(
        choices=EFFECT_TYPES,
        required=True)
    assetType = EffectPropertiesModel(required=True)
