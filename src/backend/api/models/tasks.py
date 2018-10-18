from rest_framework import serializers
from effects import EFFECTS_LIST


AFFILIATIONS = (
    "FRIENDLY", "HOSTILE"
)


class EntityModel(serializers.Serializer):
    entityId = serializers.CharField(required=True)
    entityType = serializers.CharField(required=True)


class TasksModel(serializers.Serializer):
    affiliation = serializers.ChoiceField(
        choices=AFFILIATIONS,
        required=True)
    effect = serializers.ChoiceField(
        choices=EFFECTS_LIST,
        required=True)
    assignee = EntityModel(required=True)
    objective = EntityModel(required=True)
    start = serializers.IntegerField(required=True)
    end = serializers.IntegerField(required=True)
    actionInstanceRefs = serializers.ListField(required=False)
    description = serializers.CharField(required=False)


class CourseOfActionModel(serializers.Serializer):
    missionId = serializers.CharField(required=True)
    systemId = serializers.CharField(required=True)
    tasks = TasksModel(many=True)
