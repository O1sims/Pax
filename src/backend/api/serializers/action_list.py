from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.action_list import ActionList


class ActionListSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = ActionList
        depth = 2
