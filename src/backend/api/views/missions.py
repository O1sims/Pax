import os
import pymongo as pm

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView, ListCreateAPIView
from drf_yasg.utils import swagger_auto_schema

from api.models.missions import MissionsModel


class MissionsView(ListCreateAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = MissionsModel

    def __init__(self):
        self.missions_collection = pm.MongoClient(
            host=os.environ.get('DB_HOSTNAME'),
            port=int(os.environ.get('DB_PORT'))
        )[os.environ.get('DB_NAME')]['missions']

    @swagger_auto_schema(responses={200: "OK"})
    def get(self, request, *args, **kwargs):
        missions_list = list(self.missions_collection.find())
        for mission in missions_list:
            mission['_id'] = str(mission['_id'])
        return Response(
            data=missions_list,
            status=200)

    @swagger_auto_schema(responses={201: "Created"})
    def post(self, request, *args, **kwargs):
        MissionsModel(
            data=request.data).is_valid(
            raise_exception=True)
        self.missions_collection.insert(request.data)
        return Response(status=201)


class MissionIdView(ListAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = MissionsModel

    def __init__(self):
        self.missions_collection = pm.MongoClient(
            host=os.environ.get('DB_HOSTNAME'),
            port=int(os.environ.get('DB_PORT'))
        )[os.environ.get('DB_NAME')]['missions']

    @swagger_auto_schema(responses={200: "OK"})
    def get(self, request, *args, **kwargs):
        mission = list(self.missions_collection.find(
            {"id": self.kwargs['missionId']}))
        return Response(
            data=mission,
            status=200)
