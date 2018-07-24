from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from rest_framework_mongoengine.generics import CreateAPIView

from analytics.NetworkRisk import NetworkRisk
from analytics.NetworkAnalysis import NetworkAnalysis
from analytics.RiskAnalysis import perform_system_risk_analysis, calculate_comparative_statics, \
    get_unattainable_strategies
from analytics.RiskAnalysis import remove_unattainable_strategies, calculate_dominated_strategies, \
    calculate_recommended_strategy

from api.views.c2_data_requestor import C2DataRequestor

from api.models.networks import Network, NodeRisk
from api.models.action_rest import EffectActionsCompare, EffectActions, TaskDependencyModel, \
    CoursesOfActionCompareResult
from api.models.assets import AssetRiskResult
from api.models.tasks import TasksModel


class NetworkRiskAnalysis(CreateAPIView):
    """
    Ingest a device network, run some analytics on device-level network risk,
    and return with an object containing risk scores for each device.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = Network

    @swagger_auto_schema(responses={200: NodeRisk})
    def post(self, request, *args, **kwargs):
        system_id = self.kwargs['systemId']
        device_risk_scores = NetworkRisk(
            network_data=request.data
        ).evaluate_network_risk()
        device_risk_scores.update({
            'system_id': system_id
        })
        combined_network_data = NetworkAnalysis(
            system_id=system_id
        ).combine_network_risk(
            network_data=request.data,
            device_risk_scores=device_risk_scores
        )
        NetworkAnalysis(
            system_id=system_id
        ).save_network_data(
            network_data=combined_network_data
        )
        return Response(
            data=device_risk_scores,
            status=200
        )


class SystemRiskAnalysis(C2DataRequestor):
    """
    Take a systemId, gather the system-level data from C2, find connections
    between assets and devices, and run risk analytics on assets. The endpoint
    consumes a list of tasks, which constitutes as a Course of Action.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = TasksModel

    @swagger_auto_schema(responses={200: AssetRiskResult})
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            request.data = list(request.data)

        TasksModel(
            data=request.data,
            many=True).is_valid(
            raise_exception=True)

        asset_risk = perform_system_risk_analysis(
            system_id=self.kwargs['systemId'],
            system_data=system_data,
            action_data=request.data
        )
        system_analysis = {
            "assetRisk": asset_risk
        }
        return Response(
            data=system_analysis,
            status=200
        )


class TaskDependencyRiskAnalysis(C2DataRequestor):
    """
    Allow the user to send a Course of Action with task dependencies to be
    assessed.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = TaskDependencyModel

    @swagger_auto_schema(responses={200: AssetRiskResult})
    def post(self, request, *args, **kwargs):

        data = request.data
        if isinstance(request.data, dict):
            data = list(request.data)

        request_serialize = EffectActions(data=data, many=True)
        request_serialize.is_valid(raise_exception=True)

        system_id = self.kwargs['systemId']
        return self.fetch_c2_data(data, system_id)

    def status_200(self, system_id, action_data, system_data):
        asset_risk = perform_system_risk_analysis(
            system_id=system_id,
            system_data=system_data,
            action_data=action_data
        )
        system_analysis = {
            "assetRisk": asset_risk
        }
        return Response(
            data=system_analysis,
            status=200
        )


class CompareSystemRiskAnalysis(C2DataRequestor):

    renderer_classes = (JSONRenderer,)
    serializer_class = EffectActionsCompare

    @swagger_auto_schema(responses={200: CoursesOfActionCompareResult})
    def post(self, request, *args, **kwargs):

        serializer_class = EffectActionsCompare(
            data=request.data
        )

        system_id = self.kwargs['systemId']
        return self.fetch_c2_data(request, system_id)

    def status_200(self, system_id, request, system_data):
        comparative_results = {}
        if 'missionType' in request.data.keys():
            mission_type = request.data['missionType'].lower()
        else:
            mission_type = "defensive"
        if 'restrictions' in request.data.keys():
            restrictions = request.data['restrictions']
        else:
            restrictions = {}
        comparative_statics = calculate_comparative_statics(
            system_id=system_id,
            courses_of_action=request.data['coursesOfAction'],
            system_data=system_data
        )
        unattainable_strategies = get_unattainable_strategies(
            restrictions=restrictions,
            comparative_statics=comparative_statics
        )
        new_comparative_statics = remove_unattainable_strategies(
            comparative_statics=comparative_statics,
            unattainable_strategies=unattainable_strategies
        )
        if len(new_comparative_statics) > 0:
            comparative_results['dominatedStrategies'] = calculate_dominated_strategies(
                comparative_statics=comparative_statics,
                mission_type=mission_type
            )
            comparative_results['recommendedStrategy'] = calculate_recommended_strategy(
                comparative_statics=comparative_statics,
                mission_type=mission_type
            )
        comparative_results['coaCost'] = comparative_statics
        comparative_results['unattainableStrategies'] = unattainable_strategies
        return Response(
            data=comparative_results,
            status=200
        )
