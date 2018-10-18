from rest_framework import serializers


class MissionsModel(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    criticalFunctions = serializers.ListField(required=False)
    systems = serializers.ListField(required=False)
    units = serializers.ListField(required=False)
