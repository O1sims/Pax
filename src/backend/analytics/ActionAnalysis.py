import os

import pymongo as pm


def action_force(action_list=None, effect=None):
    if action_list is None and effect is None:
        return None
    client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
    effects_collection = client[os.environ.get('DB_NAME')]['hostile_response']
    if effect is not None:
        effect_info = effects_collection.find_one({"effect": effect.upper()})
        force = effect_info['effectType']
        return force
    if action_list is not None:
        effect_info = effects_collection.find_one({"effect": action_list[0]['effect'].upper()})
        force = effect_info['effectType']
        return force


def get_action_time(effect, type):
    client = pm.MongoClient(
        host=os.environ.get('DB_HOSTNAME'),
        port=int(os.environ.get('DB_PORT'))
    )
    action_list_collection = client[os.environ.get('DB_NAME')]['action_list']
    if effect is None and type is None:
        return 50
    elif type is None:
        effect_info = action_list_collection.find_one({
            "effect": effect.upper()
        })
    elif effect is None:
        effect_info = action_list_collection.find_one({
            "type": type.upper()
        })
    else:
        effect_info = action_list_collection.find_one({
            "effect": effect.upper(),
            "type": type.lower()
        })
    effect_time = effect_info['properties']['time']
    return effect_time


def get_inherent_probability_of_success(effect, type):
    client = pm.MongoClient(
        host=os.environ.get('DB_HOSTNAME'),
        port=int(os.environ.get('DB_PORT'))
    )
    action_list_collection = client[os.environ.get('DB_NAME')]['action_list']
    effect_info = action_list_collection.find_one({"effect": effect.upper(), "type": type.lower()})
    effect_likeliness = effect_info['properties']['likeliness']
    return effect_likeliness


def task_dependencies_exist(course_of_action):
    exist = False
    if 'dependencies' in course_of_action[0].keys():
        for task in course_of_action:
            if task['dependencies']:
                exist = True
    return exist


def generate_task_name(effect, actor, start_time):
    task_id = str(effect)[:3] + '_' + str(actor)[:3] + '_' + str(int(start_time))
    return task_id
