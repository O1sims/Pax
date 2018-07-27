import config

from django.conf.urls import url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

from api.views.action_instances import ActionInstancesView
from api.views.action_templates import ActionTemplatesView
from api.views.courses_of_action import GenerateCoursesOfAction
from api.views.cvi_systems import CVIView, CVISystemView
from api.views.effects import EffectsView
from api.views.index import IndexView
from api.views.missions import MissionIdView, MissionsView
from api.views.system import SystemMissionTime
from api.views.reset import ResetData
from api.views.risk_appetite import RiskAppetiteDetail
from api.views.risk import NetworkRiskAnalysis, SystemRiskAnalysis, \
    CompareSystemRiskAnalysis, TaskDependencyRiskAnalysis


SchemaView = get_schema_view(
    openapi.Info(
        title="Pax API",
        default_version=config.API_VERSION,
        description="Pax API documentation"
    ),
    validators=['ssv', 'flex'],
    public=True
)

urlpatterns = format_suffix_patterns([
    # Risk analysis
    url(r'^api/v{}/risk_analysis/network/(?P<systemId>.+)/$'.format(
        config.API_VERSION),
        NetworkRiskAnalysis.as_view()),

    url(r'^api/v{}/risk_analysis/system/(?P<systemId>.+)/$'.format(
        config.API_VERSION),
        SystemRiskAnalysis.as_view()),

    url(r'^api/v{}/risk_analysis/task_dependency/(?P<systemId>.+)/$'.format(
        config.API_VERSION),
        TaskDependencyRiskAnalysis.as_view()),

    url(r'^api/v{}/risk_analysis/compare_system/(?P<systemId>.+)/$'.format(
        config.API_VERSION),
        CompareSystemRiskAnalysis.as_view()),

    # Effects
    url(r'^api/v{}/effects/$'.format(
        config.API_VERSION),
        EffectsView.as_view()),

    # Risk appetite
    url(r'^api/v{}/risk_appetite/(?P<missionId>.+)/$'.format(
        config.API_VERSION),
        RiskAppetiteDetail.as_view()),

    # Action templates
    url(r'^api/v{}/action_templates/$'.format(
        config.API_VERSION),
        ActionTemplatesView.as_view()),

    # Action instances
    url(r'^api/v{}/action_instances/$'.format(
        config.API_VERSION),
        ActionInstancesView.as_view()),

    # Course of action
    url(r'api/v{}/course_of_action/generate/$'.format(
        config.API_VERSION),
        GenerateCoursesOfAction.as_view()),

    # System
    url(r'^api/v{}/system/mission_time/(?P<systemId>.+)/'.format(
        config.API_VERSION),
        SystemMissionTime.as_view()),

    # CVI
    url(r'^api/v{}/cvi/'.format(
        config.API_VERSION),
        CVIView.as_view()),

    url(r'^api/v{}/cvi/(?P<systemId>.+)/'.format(
        config.API_VERSION),
        CVISystemView.as_view()),

    # Mission
    url(r'^api/v{}/missions/'.format(
        config.API_VERSION),
        MissionsView.as_view()),

    url(r'^api/v{}/missions/(?P<missionId>.+)/'.format(
        config.API_VERSION),
        MissionIdView.as_view()),

    # Reset
    url(r'^api/v{}/reset/'.format(
        config.API_VERSION),
        ResetData.as_view()),

    # Swagger
    url(r'^swagger/$',
        SchemaView.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),

    url(r'^redoc/$',
        SchemaView.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

    # Angular
    url(r'^$',
        IndexView.as_view(),
        name='index'),

    url(r'^(?P<path>.*)/$',
        IndexView.as_view()),
])
