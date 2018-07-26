from rest_framework import serializers
from tasks import AFFILIATIONS


SPECIALISM = (
    "CYBER", "PHYSICAL"
)


class UnitsModel(serializers.Serializer):
    id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    numberOfPersonnel = serializers.IntegerField(
        min_value=0,
        required=True)
    offensiveCapability = serializers.IntegerField(
        max_value=5,
        min_value=0,
        required=True)
    defensiveCapability = serializers.IntegerField(
        max_value=5,
        min_value=0,
        required=True)
    affiliation = serializers.ChoiceField(
        choices=AFFILIATIONS,
        required=True)
    specialism = serializers.ChoiceField(
        choices=SPECIALISM,
        required=True)
    equipment = serializers.ListField()
