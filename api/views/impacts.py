import os
import pymongo as pm

from rest_framework.response import Response
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView
from drf_yasg.utils import swagger_auto_schema

from api.models.impacts import Impacts
from api.serializers.impacts import ImpactsSerializer


class ImpactDetail(ListCreateAPIView, RetrieveDestroyAPIView):
    """
    Query the `impacts` collection for all documents (impacts) in the collection.
    """
    serializer_class = ImpactsSerializer

    def get_queryset(self):
        """
        Query the `impacts` collection for all documents (impacts) in the collection.
        """
        queryset = Impacts.objects.all()
        return queryset

    @swagger_auto_schema(responses={201: ""})
    def post(self, request, *args, **kwargs):
        """
        Post documents (impacts) to the `impacts` collection.
        """
        self.create(request)
        return Response(status=201)

    def delete(self, request, *args, **kwargs):
        """
        Drop the `impacts` collection.
        """
        self.queryset = Impacts.drop_collection()
        return Response(status=204)


class ImpactIdDetail(ListAPIView):
    """
    Query the `impacts` collection in Mongo for all impacts with the ID given by `impactId`.
    """
    serializer_class = ImpactsSerializer

    def get_queryset(self):
        """
        Query the `impacts` collection in Mongo for all impacts with the ID given by `impactId`.
        """
        impact_id = self.kwargs['impactId']
        if impact_id is not None:
            queryset = Impacts.objects.filter(impactId__iexact=impact_id)
        return queryset


class ImpactAssetDetail(ListAPIView):
    """
    Query the `impacts` collection in Mongo for all impacts with the asset ID given by `assetId`.
    """
    serializer_class = ImpactsSerializer

    def get(self, request, *args, **kwargs):
        asset_id = self.kwargs['assetId']
        if asset_id is not None:
            mongo_client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'),
                                          port=int(os.environ.get('DB_PORT')))
            cvi_collection = mongo_client[os.environ.get('DB_NAME')]['cvi']
            assets = list(cvi_collection.find({'assets._id': asset_id},
                                              {'_id': 0,
                                               'assets': 1}))[0]['assets']
            asset = [a for a in assets if a['_id'] == asset_id][0]
            asset_impact = asset['impact']
            asset_impact.update({
                'assetId': asset_id
            })
            return Response(asset_impact)
