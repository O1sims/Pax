from mongoengine import *
from rest_framework import serializers


class ActionList(Document):
    actions = ListField(required=False)


class EffectActions(Document):
    systemId = StringField(required=False)
    effect = StringField(required=True)
    objective = StringField(required=True)
    actor = StringField(required=True)
    timeFrame = IntField(required=True)


class EffectActionsCompare(EmbeddedDocument):
    effect = StringField(required=True)
    objective = StringField(required=True)
    actor = StringField(required=True)
    timeFrame = IntField(required=True)


class CoursesOfActionDict(EmbeddedDocument):
    COA1 = ListField(EmbeddedDocumentField(EffectActionsCompare), required=True, many=True)
    COA2 = ListField(EmbeddedDocumentField(EffectActionsCompare), required=True, many=True)
    COA3 = ListField(EmbeddedDocumentField(EffectActionsCompare), required=False, many=True)
    COA4 = ListField(EmbeddedDocumentField(EffectActionsCompare), required=False, many=True)
    COA5 = ListField(EmbeddedDocumentField(EffectActionsCompare), required=False, many=True)


class Restrictions(EmbeddedDocument):
    missionTime = IntField(required=True)
    personnel = IntField(required=True)
    probability = IntField(required=True)


class CoursesOfAction(Document):
    name = StringField(required=False)
