from math import sin, cos, sqrt, atan2, radians

from analytics.SystemAnalysis import get_asset_coordinates, get_mission_data_from_system_id


def measure_distance(lat1, long1, lat2, long2, earth_radius=6378.1):
    rlat1 = radians(lat1)
    rlong1 = radians(long1)
    rlat2 = radians(lat2)
    rlong2 = radians(long2)
    dlong = rlong2 - rlong1
    dlat = rlat2 - rlat1
    a = sin(dlat / 2)**2 + cos(rlat1) * cos(rlat2) * sin(dlong / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = earth_radius * c
    return float(format(distance, '.2f'))


def get_asset_actor_distance(system_id, asset_id, actor_id, max_distance=5):
    """
    Calculate the distance (in km) between an asset location and an actor location within a given mission.
    """
    mission_data = get_mission_data_from_system_id(
        system_id=system_id
    )
    asset_coordinates = get_asset_coordinates(
        mission_data=mission_data,
        asset_id=asset_id
    )
    actor_coordinates = get_asset_coordinates(
        mission_data=mission_data,
        asset_id=actor_id
    )
    if asset_coordinates is not None and actor_coordinates is not None:
        distance = measure_distance(
            lat1=asset_coordinates['latitude'],
            long1=asset_coordinates['longitude'],
            lat2=actor_coordinates['latitude'],
            long2=actor_coordinates['longitude']
        )
    else:
        distance = max_distance
    return distance


def calculate_actor_to_asset_time(distance, kmph=4):
    """
    Calculates the time it will take the actor to reach an asset given the distance needed to cover.
    """
    distance_time = float(distance)/float(kmph)
    return distance_time
