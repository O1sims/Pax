import json
import pymongo as pm

from data.EffectData import default_effects
from data.ActionTemplateData import default_action_templates
from data.CVISystemData import default_cvi_systems
from data.NetworkData import default_device_network
from data.RiskAppetite import default_risk_appetite
from data.MissionData import default_missions
from data.UnitData import default_units

from utils import SystemConfig as config


CLIENT = pm.MongoClient(
    host=config.DB_HOSTNAME,
    port=config.DB_PORT)


def reset_app_data():
    coll_data = {
        'effects': default_effects,
        'actionTemplates': default_action_templates,
        'cviSystems': default_cvi_systems,
        'deviceNetwork': default_device_network,
        'riskAppetite': default_risk_appetite,
        'missions': default_missions,
        'units': default_units,
        'actionInstances': None
    }
    for coll, data in coll_data.iteritems():
        reset_mongo_data(
            collection=coll,
            mongo_data=data)


def load_task_data(path):
    return_data = []
    data = json.load(open(path))
    for CoAKey, CoAData in data.items():
        for element in CoAData:
            d = {
                "taskId": element["name"],
                "objective": element["objective"]["entityId"],
                "dependencies": element["dependencies"],
                "systemId": "POWER-STATION",
                "timeFrame": element["end"] - element["start"],
                "courseOfAction": CoAKey,
                "effect": element["effect"],
                "unit": element["assignee"]["entityId"]
            }
            return_data.append(d)
    return return_data


def load_course_action_data(data):
    coa_collection = CLIENT[config.DB_NAME]['courses_of_action']
    coa_collection.drop()

    coas = []
    for task in data:
        coas.append(task['courseOfAction'])
    coas = list(set(coas))

    for coa in coas:
        coa_collection.insert({
            'systemId': "POWER-STATION",
            'name': coa
        })


def reset_mongo_data(collection, mongo_data=None):
    coll = CLIENT[config.DB_NAME][collection]
    coll.drop()
    if mongo_data:
        coll.insert(mongo_data)
