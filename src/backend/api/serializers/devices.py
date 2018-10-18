from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.devices import Devices


class DeviceDataSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = Devices
        depth = 2