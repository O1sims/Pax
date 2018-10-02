import os

import pymongo as pm

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_mongoengine.generics import ListAPIView
from drf_yasg.utils import swagger_auto_schema

from api.models.units import UnitsModel


class UnitsView(ListAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = UnitsModel

    def __init__(self):
        self.units_collection = pm.MongoClient(
            host=os.environ.get('DB_HOSTNAME'),
            port=int(os.environ.get('DB_PORT'))
        )[os.environ.get('DB_NAME')]['units']

    @swagger_auto_schema(responses={200: "OK"})
    def get(self, request, *args, **kwargs):
        units_list = list(self.units_collection.find())
        return Response(
            data=units_list,
            status=200)


def get_mission_units(mission_id):
    missions_collection = pm.MongoClient(
        host=os.environ.get('DB_HOSTNAME'),
        port=int(os.environ.get('DB_PORT'))
    )[os.environ.get('DB_NAME')]['missions']
    
