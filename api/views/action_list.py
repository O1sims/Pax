import os

import pymongo as pm

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_mongoengine.generics import ListAPIView, UpdateAPIView
from drf_yasg.utils import swagger_auto_schema

from api.models.action_list import ActionList


class ActionListDetail(ListAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = ActionList

    def __init__(self):
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        self.action_list_collection = client[os.environ.get('DB_NAME')]['action_list']

    def get(self, request):
        action_list = list(self.action_list_collection.find({}, {"_id": 0}))
        return Response(data=action_list, status=200)

    # Implement the get_queryset to stop warnings of schema generation
    def get_queryset(self):
        return None


class ActionListForceDetail(ListAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = ActionList

    def __init__(self):
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        self.action_list_collection = client[os.environ.get('DB_NAME')]['action_list']

    def get(self, request, *args, **kwargs):
        force = self.kwargs['force']
        action_list = list(self.action_list_collection.find({"force": force}, {"_id": 0}))
        return Response(data=action_list, status=200)


class ActionListForceEffectDetail(ListAPIView, UpdateAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = ActionList

    def __init__(self):
        client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
        self.action_list_collection = client[os.environ.get('DB_NAME')]['action_list']

    def get(self, request, *args, **kwargs):
        force = self.kwargs['force']
        type = self.kwargs['type']
        effect = self.kwargs['effect'].upper()
        action_list = list(self.action_list_collection.find({"force": force, "effect": effect, "type": type}, {"_id": 0}))
        return Response(data=action_list, status=200)

    @swagger_auto_schema(responses={200: ""})
    def patch(self, request, *args, **kwargs):
        force = self.kwargs['force']
        type = self.kwargs['type']
        effect = self.kwargs['effect'].upper()
        action_body = request.data
        self.action_list_collection.update({"force": force, "effect": effect, "type": type}, {"$set": action_body})
        return Response(status=200)

