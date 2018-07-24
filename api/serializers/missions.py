from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.missions import Missions


class MissionDataSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = Missions
        depth = 2