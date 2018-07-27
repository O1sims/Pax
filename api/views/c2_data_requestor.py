import os
import json
import requests

from rest_framework.response import Response
from rest_framework_mongoengine.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer

from api.models.cvi_systems import CVISystemModel

from api.services.system_data import get_system_data

from utils import SystemConfig as config


class C2DataRequestor(CreateAPIView):
    renderer_classes = (JSONRenderer,)

    def fetch_c2_data(self, request, system_id):

        response = requests.get(
            url="http://{}/system/{}".format(
                os.environ.get('C2_REST'),
                system_id))

        if response.status_code == 200:
            system_data = response.json()
            CVISystemModel(
                data=system_data
            ).is_valid(
                raise_exception=True)
        else:
            raise ValueError("Could not find system data from C2")

        system_data = get_system_data(
            system_id=system_id)

        return self.status_200(system_id, request, system_data)

    def missing_keys(self, missing_keys):
        context = {
            "Message": "Missing the follow keys from C2 data request:",
            "MissingKeys": missing_keys
        }
        return Response(data=context, status=409)

    def c2_error(self, result):
        data = None

        try:
            data = result.json()
        except ValueError:
            pass

        context = {
            "Message": "There was an error from the c2 api",
            "c2_error_code": result.status_code,
            "c2_pay_load": data
        }
        return Response(data=context, status=400)
