import os
import pymongo as pm

from bson import ObjectId
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.models.effects import EffectsModel
from api.views.action_instances import MONGO_ID_R


EFFECT_TYPE = openapi.Parameter(
    name='type',
    in_=openapi.IN_QUERY,
    description='An effect name such as DESTROY',
    type=openapi.TYPE_STRING,
    required=False)

EFFECT = openapi.Parameter(
    name='effect',
    in_=openapi.IN_QUERY,
    description='Either "offensive" or "defensive"',
    type=openapi.TYPE_STRING,
    required=False)

MONGO_ID = openapi.Parameter(
    name='_id',
    in_=openapi.IN_QUERY,
    description='A Mongo ID string',
    type=openapi.TYPE_STRING,
    required=False)


class EffectsView(RetrieveUpdateDestroyAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = EffectsModel

    def __init__(self):
        self.effects_collection = pm.MongoClient(
            host=os.environ.get('DB_HOSTNAME'),
            port=int(os.environ.get('DB_PORT'))
        )[os.environ.get('DB_NAME')]['effects']

    @swagger_auto_schema(manual_parameters=[EFFECT, EFFECT_TYPE, MONGO_ID])
    def get(self, request, *args, **kwargs):
        query_params = dict(self.request.GET.iteritems())
        if len(query_params) > 0:
            if '_id' in query_params.keys():
                query_params['_id'] = ObjectId(query_params['_id'])
            effect_list = list(self.effects_collection.find(query_params))
        else:
            effect_list = list(self.effects_collection.find())
        for effect in effect_list:
            effect["_id"] = str(effect["_id"])
        return Response(
            data=effect_list,
            status=200)

    def put(self, request, *args, **kwargs):
        EffectsModel(
            data=request.data).is_valid(
            raise_exception=True)
        self.effects_collection.insert(request.data)
        return Response(status=201)

    @swagger_auto_schema(manual_parameters=[MONGO_ID_R])
    def patch(self, request, *args, **kwargs):
        EffectsModel(
            data=request.data).is_valid(
            raise_exception=True)
        mongo_id = self.request.GET.get('_id', None)
        if mongo_id is None:
            raise ValueError("Please provide a Mongo ID as query parameter (id)")
        self.effects_collection.update(
            {'_id': ObjectId(mongo_id)},
            {"$set": request.data},
            upsert=False)
        return Response(status=204)

    @swagger_auto_schema(manual_parameters=[MONGO_ID_R])
    def delete(self, request, *args, **kwargs):
        mongo_id = self.request.GET.get('_id', None)
        effect_name = self.request.GET.get('name', None)
        if mongo_id is None and effect_name is None:
            raise ValueError("Please provide a Mongo ID or effect name as query parameter (id, name)")
        elif mongo_id is not None:
            self.effects_collection.delete_one(
                {'_id': ObjectId(mongo_id)})
        elif effect_name is not None:
            self.effects_collection.delete_one(
                {'name': effect_name})
        return Response(status=204)
