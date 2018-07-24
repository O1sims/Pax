from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.system import System, Network


class SystemSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = System
        depth = 2


class NetworkSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = Network
        depth = 2
