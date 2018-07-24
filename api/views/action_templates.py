import os
import ast

import pymongo as pm

from bson import ObjectId
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.models.action_templates import ActionTemplatesModel
from api.views.action_instances import MONGO_ID_R, MONGO_IDS


class ActionTemplatesView(RetrieveUpdateDestroyAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = ActionTemplatesModel

    def __init__(self):
        self.action_templates_collection = pm.MongoClient(
            host=os.environ.get('DB_HOSTNAME'),
            port=int(os.environ.get('DB_PORT'))
        )[os.environ.get('DB_NAME')]['actionTemplates']

    @swagger_auto_schema(manual_parameters=[MONGO_IDS])
    def get(self, request, *args, **kwargs):
        mongo_ids = self.request.GET.get('ids', None)
        if mongo_ids:
            mongo_ids = [ObjectId(x) for x in ast.literal_eval(mongo_ids)]
            action_templates_list = list(self.action_templates_collection.find(
                {"_id": {"$in": mongo_ids}}))
        else:
            action_templates_list = list(self.action_templates_collection.find())
        for template in action_templates_list:
            template["_id"] = str(template["_id"])
        return Response(
            data=action_templates_list,
            status=200)

    @swagger_auto_schema(responses={201: "Created"})
    def put(self, request, *args, **kwargs):
        ActionTemplatesModel(
            data=request.data).is_valid(
            raise_exception=True)
        self.action_templates_collection.insert(request.data)
        return Response(status=201)

    @swagger_auto_schema(manual_parameters=[MONGO_ID_R], responses={204: "No content"})
    def patch(self, request, *args, **kwargs):
        ActionTemplatesModel(
            data=request.data).is_valid(
            raise_exception=True)
        mongo_id = self.request.GET.get('id', None)
        if mongo_id is None:
            raise ValueError("Please provide a Mongo ID as query parameter (_id)")
        self.action_templates_collection.update(
            {'_id': ObjectId(mongo_id)},
            {"$set": request.data},
            upsert=False)
        return Response(status=204)

    @swagger_auto_schema(manual_parameters=[MONGO_ID_R], responses={204: "No content"})
    def delete(self, request, *args, **kwargs):
        mongo_id = self.request.GET.get('id', None)
        if mongo_id is None:
            raise ValueError("Please provide a Mongo ID as query parameter (_id)")
        self.action_templates_collection.delete_one(
            {'_id': ObjectId(mongo_id)})
        return Response(status=204)
