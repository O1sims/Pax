import os

import pymongo as pm


def action_time_map():
    client = pm.MongoClient(host=os.environ.get('DB_HOSTNAME'), port=int(os.environ.get('DB_PORT')))
    action_list_collection = client[os.environ.get('DB_NAME')]['action_list']
    action_list = list(action_list_collection.find())
    action_time = {}
    for action in action_list:
        action_time.update({
            action['effect']: action['properties']['time']
        })
    return action_time


def risk_label_from_score(risk_score):
    if risk_score >= 80:
        return 'Critical'
    elif risk_score >= 60:
        return 'High'
    elif risk_score >= 40:
        return 'Medium'
    elif risk_score >= 20:
        return 'Low'
    else:
        return 'Very low'


def criticality_label_from_score(criticality_score):
    if criticality_score >= 80:
        return 'Critical'
    elif criticality_score >= 60:
        return 'High'
    elif criticality_score >= 40:
        return 'Medium'
    elif criticality_score >= 20:
        return 'Low'
    else:
        return 'Very low'


def probability_label_from_score(probability):
    if probability >= 80:
        return 'Very high'
    elif probability >= 60:
        return 'High'
    elif probability >= 40:
        return 'Medium'
    elif probability >= 20:
        return 'Low'
    else:
        return 'Very low'


def threat_label_level_map(threat_label=None, threat_level=None):
    threat_label_map = {
        'critical': 6,
        'high': 5,
        'severe': 4,
        'substantial': 3,
        'moderate': 2,
        'no': 1
    }
    if threat_label is not None:
        threat_label_lower = threat_label.lower()
        return threat_label_map[threat_label_lower]
    elif threat_level is not None:
        for label in threat_label_map:
            if threat_label_map[label] == threat_level:
                return label

