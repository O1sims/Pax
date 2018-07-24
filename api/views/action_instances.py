import os
import ast
import pymongo as pm

from bson import ObjectId
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.models.action_instances import ActionInstancesModel


MONGO_IDS = openapi.Parameter(
    name='_ids',
    in_=openapi.IN_QUERY,
    description='A list of Mongo ID strings',
    type=openapi.TYPE_STRING,
    required=False)

MONGO_ID_R = openapi.Parameter(
    name='_id',
    in_=openapi.IN_QUERY,
    description='A single Mongo ID string',
    type=openapi.TYPE_STRING,
    required=True)


class ActionInstancesView(RetrieveUpdateDestroyAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = ActionInstancesModel

    def __init__(self):
        self.action_instances_collection = pm.MongoClient(
            host=os.environ.get('DB_HOSTNAME'),
            port=int(os.environ.get('DB_PORT'))
        )[os.environ.get('DB_NAME')]['actionInstances']

    @swagger_auto_schema(manual_parameters=[MONGO_IDS])
    def get(self, request, *args, **kwargs):
        mongo_ids = self.request.GET.get('_ids', None)
        if mongo_ids:
            mongo_ids = [ObjectId(x) for x in ast.literal_eval(mongo_ids)]
            action_instances_list = list(self.action_instances_collection.find(
                {"_id": {"$in": mongo_ids}}))
        else:
            action_instances_list = list(self.action_instances_collection.find())
        for instance in action_instances_list:
            instance["_id"] = str(instance["_id"])
        return Response(
            data=action_instances_list,
            status=200)

    @swagger_auto_schema(responses={201: "Created"})
    def put(self, request, *args, **kwargs):
        ActionInstancesModel(
            data=request.data).is_valid(
            raise_exception=True)
        self.action_instances_collection.insert(request.data)
        return Response(status=201)

    @swagger_auto_schema(manual_parameters=[MONGO_ID_R], responses={204: "No content"})
    def patch(self, request, *args, **kwargs):
        ActionInstancesModel(
            data=request.data).is_valid(
            raise_exception=True)
        mongo_id = self.request.GET.get('_id', None)
        if mongo_id is None:
            raise ValueError("Please provide a Mongo ID as query parameter (_id)")
        self.action_instances_collection.update(
            {'_id': ObjectId(mongo_id)},
            {"$set": request.data},
            upsert=False)
        return Response(status=204)

    @swagger_auto_schema(manual_parameters=[MONGO_ID_R], responses={204: "No content"})
    def delete(self, request, *args, **kwargs):
        mongo_id = self.request.GET.get('_id', None)
        if mongo_id is None:
            raise ValueError("Please provide a Mongo ID as query parameter (_id)")
        self.action_instances_collection.delete_one(
            {'_id': ObjectId(mongo_id)})
        return Response(status=204)
