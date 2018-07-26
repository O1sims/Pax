from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.cvi import Cvi


class CviSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = Cvi
        depth = 2
