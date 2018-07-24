from mongoengine import *


class Missions(Document):
    missionId = StringField(required=False)
    missionRisk = DictField(required=False)
    missionObjective = StringField(required=False)
    missionRiskTimeline = ListField(required=False)
