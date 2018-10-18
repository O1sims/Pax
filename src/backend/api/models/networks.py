from rest_framework import serializers


class Network(serializers.Serializer):
    nodes = serializers.ListField(required=False)
    edges = serializers.ListField(required=False)


class RiskLabel(serializers.Serializer):
    riskLabel = serializers.CharField(required=False)
    riskScore = serializers.IntegerField(min_value=0, required=False)


class NodeRisk(serializers.Serializer):
    nodeID = RiskLabel(required=False, many=True)