from rest_framework import serializers


ACTION_TYPES = (
    "physical", "cyber", "actor"
)


class ActionTemplatesModel(serializers.Serializer):
    name = serializers.CharField(required=True)
    type = serializers.ChoiceField(
        choices=ACTION_TYPES,
        required=True)
    description = serializers.CharField(required=True)
