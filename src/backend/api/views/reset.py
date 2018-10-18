from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import CreateAPIView

from utils.MongoDataLoader import reset_app_data
from drf_yasg.utils import swagger_auto_schema

from api.models.reset import ResetModel


class ResetData(CreateAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = ResetModel

    @swagger_auto_schema(request_body=ResetModel, responses={201: "Data reset"})
    def post(self, request, *args, **kwargs):
        reset_app_data()
        return Response(status=201)
