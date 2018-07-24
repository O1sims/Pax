from rest_framework import serializers


RESOURCE_USE_LEVELS = (
    "high", "medium", "low"
)


class ActionMetaDataModel(serializers.Serializer):
    resourceUse = serializers.ChoiceField(
        choices=RESOURCE_USE_LEVELS,
        required=True)
    timeTaken = serializers.IntegerField(required=True)
    probabilityOfSuccess = serializers.IntegerField(required=True)


class ActionInstancesModel(serializers.Serializer):
    actionTemplateRefs = serializers.ListField(required=True)
    metaData = ActionMetaDataModel(required=True)
