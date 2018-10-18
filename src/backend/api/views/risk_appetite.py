import os
import pymongo as pm

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from analytics.RiskAppetite import RiskAppetiteAnalysis
from api.serializers.risk_appetite import RiskAppetiteSerializer


class RiskAppetiteDetail(RetrieveUpdateDestroyAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = RiskAppetiteSerializer

    def __init__(self):
        self.risk_appetite_collection = pm.MongoClient(
            host=os.environ.get('DB_HOSTNAME'),
            port=int(os.environ.get('DB_PORT'))
        )[os.environ.get('DB_NAME')]['riskAppetite']

    def get(self, request, *args, **kwargs):
        mission_id = self.kwargs['missionId']
        if mission_id in None:
            risk_appetite_data = self.risk_appetite_collection.find()
        else:
            risk_appetite_data = self.risk_appetite_collection.find(
                {'missionId': mission_id})
        return Response(
            data=risk_appetite_data,
            status=200)

    def put(self, request, *args, **kwargs):
        risk_appetite_score = RiskAppetiteAnalysis(
            risk_appetite_data=request.data).generate_risk_appetite_score()
        request.data.update({
            'riskAppetiteScore': risk_appetite_score,
            'riskAppetiteLabel': RiskAppetiteAnalysis(
                risk_appetite_data=request.data).generate_risk_appetite_label(
                riskAppetiteScore=risk_appetite_score)
        })
        self.risk_appetite_collection.insert(request.data)
        return Response(status=201)

    def patch(self, request, *args, **kwargs):
        self.risk_appetite_collection.update({
            'missionId': self.kwargs['missionId']},
            {"$set": request.data},
            upsert=False)
        return Response(data=204)

    def delete(self, request, *args, **kwargs):
        self.risk_appetite_collection.delete_one({
            'missionId': self.kwargs['missionId']})
        return Response(status=204)
