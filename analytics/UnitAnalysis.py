import os
import requests


def get_unit_data(unit_id):
    r = requests.get('http://' + os.environ.get('C2_REST') + 'entity/Unit/' + unit_id)
    unit_data = r.json()
    return unit_data


def get_hostile_unit():
    r = requests.get('http://' + os.environ.get('C2_REST') + 'entity/Unit/')
    unit_data = r.json()
    hostile_units = [
        unit for unit in unit_data if unit['affiliation'] == 'HOSTILE'
    ]
    hostile_unit = hostile_units[0]
    return hostile_unit
