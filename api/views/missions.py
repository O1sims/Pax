from rest_framework.response import Response
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView

from api.models.missions import Missions
from api.serializers.missions import MissionDataSerializer


class MissionDetail(ListCreateAPIView, RetrieveDestroyAPIView):
    """
    Query the `missions` collection in Mongo.
    """
    serializer_class = MissionDataSerializer

    def get_queryset(self):
        """
        Collect all documents (missions) from the `missions` collection in Mongo.
        """
        queryset = Missions.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        """
        Store mission data in the `missions` collection in Mongo.
        """
        self.create(request, *args, **kwargs)
        return Response(status=201)

    def delete(self, request, *args, **kwargs):
        """
        Drop the `missions` Mongo collection.
        """
        self.queryset = Missions.drop_collection()
        return Response(status=204)


class MissionIdDetail(ListAPIView):
    """
    Query the `missions` collection in Mongo by mission ID, given by `missionID`.
    """
    serializer_class = MissionDataSerializer

    def get_queryset(self):
        mission_id = self.kwargs['missionId']
        if mission_id is not None:
            queryset = Missions.objects.filter(missionId__iexact=mission_id)
        return queryset


class MissionObjectiveDetail(ListAPIView):
    """
    Query the `missions` collection in Mongo by mission objective, given by `missionObjective`.
    """
    serializer_class = MissionDataSerializer

    def get_queryset(self):
        mission_objective = self.kwargs['missionObjective']

        if mission_objective is not None:
            queryset = Missions.objects.filter(missionObjective__iexact=mission_objective)
        return queryset
