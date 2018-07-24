from mongoengine import *


class Impacts(Document):
    assetName = StringField(required=False)
    assetId = StringField(required=False)
    availability = StringField(required=False)
    confidentiality = StringField(required=False)
    criticality = StringField(required=False)
    integrity = StringField(required=False)
    impactId = StringField(required=False)
