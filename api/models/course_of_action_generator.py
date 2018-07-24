from rest_framework import serializers


search_data = (
    (
        "depth",
        "Depth based task discovery"
    ), (
        "breadth",
        "Breadth base task discovery"
    )
)


class Task(serializers.Serializer):
    taskId = serializers.CharField(required=True)
    effect = serializers.CharField(required=True)
    objective = serializers.CharField(required=False)
    actor = serializers.CharField(required=False)
    timeFrame = serializers.IntegerField(min_value=0, required=False)
    dependencies = serializers.ListField(child=serializers.CharField(), required=True)


class CourseOfActionGeneration(serializers.Serializer):
    target_task = Task(required=True)
    tasks = serializers.ListField(child=Task(), required=False)
    type = serializers.CharField(default="depth")


class ListOfTasks(serializers.Serializer):
    tasks = serializers.ListField(child=Task(), required=False)
