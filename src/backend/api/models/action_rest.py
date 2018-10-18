from rest_framework import serializers
from tasks import TasksModel


class EffectActions(serializers.Serializer):
    taskId = serializers.CharField(required=False)
    effect = serializers.CharField(required=False)
    objective = serializers.CharField(required=False)
    actor = serializers.CharField(required=False)
    timeFrame = serializers.IntegerField(min_value=0, required=False)
    dependencies = serializers.ListField(required=False)


class DependencyList(serializers.ListField):
    taskId = serializers.CharField()


class TaskDependencyModel(serializers.Serializer):
    taskId = serializers.CharField(required=False)
    effect = serializers.CharField(required=False)
    objective = serializers.CharField(required=False)
    actor = serializers.CharField(required=False)
    timeFrame = serializers.IntegerField(min_value=0, required=False)
    dependencies = DependencyList(required=False)


class EffectActionsElement(serializers.Serializer):
    taskId = serializers.CharField(required=True)
    effect = serializers.CharField(required=True)
    objective = serializers.CharField(required=True)
    actor = serializers.CharField(required=True)
    timeFrame = serializers.IntegerField(min_value=0, required=True)
    dependencies = serializers.ListField(required=False)


class Restrictions(serializers.Serializer):
    missionTime = serializers.IntegerField(min_value=0, required=False)
    personnel = serializers.IntegerField(min_value=0, required=False)
    probability = serializers.IntegerField(min_value=0, required=False)


class CoursesOfActionDict(serializers.Serializer):
    name = serializers.CharField(required=True)
    id = serializers.CharField(required=True)
    tasks = EffectActions(required=True, many=True)


MISSION_CHOICES = (
    'defensive',
    'offensive'
)


class EffectActionsCompare(serializers.Serializer):
    coursesOfAction = CoursesOfActionDict(many=True, required=True)
    missionType = serializers.ChoiceField(choices=MISSION_CHOICES, required=True)
    restrictions = Restrictions(required=False)


class ComparativeStatics(serializers.Serializer):
    courseOfAction = serializers.CharField(required=False)
    totalTime = serializers.IntegerField(min_value=0, required=False)
    totalRisk = serializers.IntegerField(min_value=0, required=False)
    unitsRequired = serializers.IntegerField(min_value=0, required=False)
    probabilityOfCompletion = serializers.IntegerField(min_value=0, required=False)


class UnattainableStrategies(serializers.Serializer):
    courseOfAction = serializers.CharField(required=False)
    reason = serializers.ListField(child=serializers.CharField(), required=False)


class CoursesOfActionCompareResult(serializers.Serializer):
    recommendedStrategy = serializers.CharField(required=False)
    dominatedStrategies = EffectActions(required=False),
    comparativeStatics = serializers.ListField(child=ComparativeStatics(), required=False)
    UnattainableStrategies = serializers.ListField(child=UnattainableStrategies(), required=False)


class MissionTimeModel(serializers.Serializer):
    missionTime = serializers.IntegerField(required=True)
    courseOfAction = TasksModel(required=True, many=True)


class ExceedsTime(serializers.Serializer):
    exceedsTime = serializers.BooleanField()
