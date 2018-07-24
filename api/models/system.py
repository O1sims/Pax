from mongoengine import *


class System(Document):
    name = StringField(required=False)
    description = StringField(required=False)
    groups = ListField(required=False)
    functions = ListField(required=False)
    assets = ListField(required=False)
    threats = ListField(required=False)
    vulnerabilities = ListField(required=False)


class Network(Document):
    nodes = ListField(required=False)
    edges = ListField(required=False)

