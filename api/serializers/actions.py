from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.actions import ActionList, CoursesOfAction, EffectActions


class ActionListSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = ActionList
        depth = 2


class EffectActionsSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = EffectActions
        depth = 2


class CoursesOfActionSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = CoursesOfAction
        depth = 2
