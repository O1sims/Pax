from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.risk_appetite import RiskAppetite


class RiskAppetiteSerializer(DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = RiskAppetite
        depth = 2
