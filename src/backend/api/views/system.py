from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_mongoengine.generics import CreateAPIView

from api.models.action_rest import MissionTimeModel, ExceedsTime

from analytics.ActionAnalysis import task_dependencies_exist, get_action_time
from analytics.Geolocation import get_asset_actor_distance, calculate_actor_to_asset_time
from analytics.SystemAnalysis import exceeds_mission_time, asset_from_id
from api.services.system_data import get_system_data


@swagger_auto_schema(responses={201: ExceedsTime})
class SystemMissionTime(CreateAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = MissionTimeModel

    def post(self, request, *args, **kwargs):
        MissionTimeModel(
            data=request.data
        ).is_valid(
            raise_exception=True)
        assets = get_system_data(
            system_id=self.kwargs['systemId'],
            component='assets')
        for task in request.data['courseOfAction']:
            task['timeFrame'] = task['end'] - task['start']
            task['calculatedTimeFrame'] = get_calculated_time_frame(
                system_id=self.kwargs['systemId'],
                task=task,
                assets=assets)
        dependencies_exist = task_dependencies_exist(
            course_of_action=request.data['courseOfAction'])
        proposed_total_time = request.data['missionTime']
        calculated_total_time = exceeds_mission_time(
            course_of_action=request.data['courseOfAction'],
            dependencies=dependencies_exist)
        task_times = estimate_task_times(
            course_of_action=request.data['courseOfAction'])
        if proposed_total_time > calculated_total_time:
            exceeds_time = False
        else:
            exceeds_time = True
        return Response(
            data={
                'proposedTotalTime': proposed_total_time,
                'calculatedTotalTime': calculated_total_time,
                'exceedsTime': exceeds_time,
                'taskTimes': task_times
            },
            status=201)


def get_calculated_time_frame(system_id, task, assets):
    if task['effect'].upper() == 'MOVE':
        distance = get_asset_actor_distance(
            system_id=system_id,
            asset_id=task['objective']['entityId'],
            actor_id=task['assignee']['entityId'])
        distance_time = calculate_actor_to_asset_time(
            distance=distance)
        return distance_time

    if task['objective']['entityType'] == 'asset':
        objective_type = asset_from_id(
            asset_id=task['objective']['entityId'],
            assets=assets,
            asset_type=True)
        calculated_time_frame = get_action_time(
            effect=task['effect'],
            type=objective_type)
    elif task['objective']['entityType'] == 'systemFunction':
        objective_types = asset_types_allocated_to_function(
            function_id=task['objective']['entityId'],
            assets=assets)
        calculated_time_frame = 0
        if len(objective_types) > 0:
            for objective_type in objective_types:
                calculated_time_frame += get_action_time(
                    effect=task['effect'],
                    type=objective_type)
        else:
            calculated_time_frame = 53
    return calculated_time_frame


def estimate_task_times(course_of_action):
    task_times = []
    for task in course_of_action:
        task_times.append({
            'id': task['id'],
            'proposedTimeTaken': task['timeFrame'],
            'calculatedTimeTaken': task['calculatedTimeFrame']
        })
    return task_times


def asset_types_allocated_to_function(function_id, assets):
    asset_types = []
    for asset in assets:
        if asset['function'] == function_id:
            asset_types.append(
                asset['assetType']
            )
    return asset_types
