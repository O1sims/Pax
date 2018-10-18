from mongoengine import *


class Devices(Document):
    external = BooleanField(required=False)
    globalId = StringField(required=False)
    function = StringField(required=False)
    facility = StringField(required=False)
    ipAddress = StringField(required=False)
    machineClass = StringField(required=False)
    name = StringField(required=False)
    os = StringField(required=False)
    platform = StringField(required=False)
    type = StringField(required=False)
    unit = StringField(required=False)
    currentRiskScore = FloatField(required=False)
    vulnerabilityRisk = FloatField(required=False)
    vulnerabilities = ListField(required=False)
    subnet = StringField(required=False)
    exists = IntField(required=False)
