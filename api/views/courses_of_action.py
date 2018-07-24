import os

import pymongo as pm
import requests as re

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveDestroyAPIView
from drf_yasg.utils import swagger_auto_schema

from api.serializers.actions import CoursesOfActionSerializer
from api.models.course_of_action_generator import CourseOfActionGeneration, ListOfTasks
from utils import SystemConfig as config

from analytics import CourseOfActionGeneration as COAG
from analytics.SystemAnalysis import get_mission_data_from_system_id


class CoursesOfActionDetail(ListCreateAPIView, RetrieveDestroyAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = CoursesOfActionSerializer

    def get(self, request, *args, **kwargs):
        mission_data = get_mission_data_from_system_id(
            system_id=self.kwargs['systemId']
        )
        courses_of_action = []
        for coa in mission_data['coAs']:
            courses_of_action.append(coa['name'])
        return Response(
            data=courses_of_action,
            status=200
        )

    def post(self, request, *args, **kwargs):
        mission_id = get_mission_data_from_system_id(
            system_id=self.kwargs['systemId'],
            id_only=True
        )
        re.post(
            'http://' + os.environ.get('C2_REST') + 'coa/mission/' + mission_id + '/coa/' + request.data['name']
        )
        return Response(
            status=201
        )

    def delete(self, request, *args, **kwargs):
        mission_data = get_mission_data_from_system_id(
            system_id=self.kwargs['systemId']
        )
        mission_id = mission_data['globalId']
        for coa in mission_data['coAs']:
            if coa['name'] == request.data['name']:
                re.delete(
                    'http://' + os.environ.get('C2_REST') + 'coa/mission/' + mission_id + '/coa/' + coa['id']
                )
        return Response(
            status=204
        )


class GenerateCoursesOfAction(ListCreateAPIView):

    renderer_classes = (JSONRenderer,)
    serializer_class = CourseOfActionGeneration

    def __init__(self):
        client = pm.MongoClient(host=config.DB_HOSTNAME, port=config.DB_PORT)
        self.tasks_collection = client[config.DB_NAME]['action_list']

    @swagger_auto_schema(responses={201: ListOfTasks})
    def post(self, request, *args, **kwargs):

        serializer = CourseOfActionGeneration(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = request.data
        print data["type"]
        if not data["type"]=="depth" and not data["type"]=="breadth":
            context = {
                "message": '"type" field must be "depth" or "breadth"'
            }
            return Response(status=400, data=context)

        tasks = None
        if "tasks" in data:
            tasks = data["tasks"]

        if tasks is None:
            tasks = list(self.tasks_collection.find({}, {"_id":False}))


        dep_fun = getattr(COAG, "generate_course_action_" + data["type"])

        result = dep_fun(data["target_task"], tasks)

        task_list = COAG.extract_tasks(result, tasks)

        return Response(status=201, data=task_list)
