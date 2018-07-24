from rest_framework import serializers

class Properties(serializers.Serializer):
    likeliness = serializers.IntegerField(required=False, min_value=0)
    time = serializers.IntegerField(required=False, min_value=0)


class ActionList(serializers.Serializer):
    type = serializers.CharField(required=False)
    force = serializers.CharField(required=False)
    effect = serializers.CharField(required=False)
    actions = serializers.ListField(required=False,
                                    child=serializers.CharField())
    properties = Properties(required=False)
