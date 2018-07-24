from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.impacts import Impacts


class ImpactsSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = Impacts
        depth = 2