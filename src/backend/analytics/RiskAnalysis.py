from analytics.UnitAnalysis import get_unit_data
from analytics.ActionAnalysis import get_action_time
from analytics.SystemRisk import evaluate_system_risk, task_likelihood_from_risk_data
from analytics.SystemAnalysis import asset_from_id, remove_asset_vulnerabilities, add_asset_threats


unattainable_strategies_messages = {
    "time": " The time taken to achieve this course of action is too long",
    "personnel": "Too many personnel are needed to achieve this course of action",
    "probability": "The probability of completing this course of action is too low"
}


def perform_system_risk_analysis(system_id, system_data, action_data=None):
    if action_data == {} or action_data is None:
        asset_risk = evaluate_system_risk(
            system_id=system_id,
            system_data=system_data)
    else:
        new_system_data = update_system_data(
            system_data=system_data,
            action_data=action_data)
        asset_risk = evaluate_system_risk(
            system_id=system_id,
            system_data=new_system_data,
            action_data=action_data)
    return asset_risk


def update_system_data(system_data, action_data):
    new_system_data_v = remove_asset_vulnerabilities(
        system_data=system_data,
        action_data=action_data)
    new_system_data_t = add_asset_threats(
        system_data=new_system_data_v,
        action_data=action_data)
    return new_system_data_t


def get_unattainable_strategies(restrictions, comparative_statics):
    unattainable_strategies = []
    if len(restrictions) > 0:

        for coa in comparative_statics:
                reason = []
                if coa['totalTime'] > restrictions['missionTime']:
                    reason.append(unattainable_strategies_messages["time"])
                if coa['unitsRequired'] > restrictions['personnel']:
                    reason.append(unattainable_strategies_messages["personnel"])
                if coa['probabilityOfCompletion'] < restrictions['probability']:
                    reason.append(unattainable_strategies_messages["probability"])

                if len(reason) == 0:
                    continue

                unattainable_strategies.append({
                    'courseOfAction': coa['courseOfAction'],
                    'reason': reason
                })

    return unattainable_strategies


def remove_unattainable_strategies(comparative_statics, unattainable_strategies):

    for unattainable in unattainable_strategies:
        for coa in comparative_statics:
            if unattainable['courseOfAction'] == coa['courseOfAction']:
                comparative_statics.remove(coa)

    return comparative_statics


def calculate_comparative_statics(system_id, courses_of_action, system_data):
    comparative_statics = []
    initial_asset_risk = perform_system_risk_analysis(
        system_id=system_id,
        system_data=system_data
    )
    for coa in courses_of_action:
        asset_risk = perform_system_risk_analysis(
            system_id=system_id,
            system_data=system_data,
            action_data=coa['tasks']
        )
        comparative_object = {
            'courseOfAction': coa['name'],
            'totalRisk': 0,
            'totalTime': 0,
            'probabilityOfCompletion': 0,
            'unitsRequired': 0
        }
        joint_probability = []
        for task in coa['tasks']:
            objective_type = asset_from_id(
                asset_id=task['objective'],
                assets=system_data['assets'],
                asset_type=True
            )
            comparative_object['totalTime'] += get_action_time(
                effect=task['effect'],
                type=objective_type
            )
            likelihood_of_failure = task_likelihood_from_risk_data(
                risk_data=asset_risk,
                task=task
            )
            joint_probability.append(float(100 - likelihood_of_failure) / float(100))
        comparative_object['probabilityOfCompletion'] = 100 * (reduce(lambda x, y: x * y, joint_probability))
        for asset in initial_asset_risk:
            comparative_object['totalRisk'] += (asset_risk[asset]['risks'][0]['riskScore'] -
                                                initial_asset_risk[asset]['risks'][0]['riskScore'])
        comparative_object['unitsRequired'] = calculate_units_required(
            course_of_action=coa['tasks']
        )
        comparative_statics.append(comparative_object)
    return comparative_statics


def calculate_dominated_strategies(comparative_statics, mission_type):
    dominated_strategies = {}
    if mission_type == 'offensive':
        for COA in comparative_statics:
            dominated_by = []
            for newCOA in comparative_statics:
                if newCOA != COA:
                    if COA['totalTime'] >= newCOA['totalTime'] and \
                            COA['totalRisk'] <= newCOA['totalRisk'] and \
                            COA['unitsRequired'] >= newCOA['unitsRequired'] and \
                            COA['probabilityOfCompletion'] <= newCOA['probabilityOfCompletion']:
                        dominated_by.append(newCOA['courseOfAction'])
            if len(dominated_by) == 0:
                dominated_by = None
            dominated_strategies.update({
                COA['courseOfAction']: dominated_by
            })
    if mission_type == 'defensive':
        for COA in comparative_statics:
            dominated_by = []
            for newCOA in comparative_statics:
                if newCOA != COA:
                    if COA['totalTime'] >= newCOA['totalTime'] and \
                            COA['totalRisk'] >= newCOA['totalRisk'] and \
                            COA['unitsRequired'] >= newCOA['unitsRequired'] and \
                            COA['probabilityOfCompletion'] <= newCOA['probabilityOfCompletion']:
                        dominated_by.append(newCOA['courseOfAction'])
            if len(dominated_by) == 0:
                dominated_by = None
            dominated_strategies.update({
                COA['courseOfAction']: dominated_by
            })
    return dominated_strategies


def calculate_recommended_strategy(comparative_statics, mission_type):
    best_coa = comparative_statics[0]['courseOfAction']
    best_total_risk = comparative_statics[0]['totalRisk']
    if mission_type == 'offensive':
        for COA in comparative_statics:
            if COA['totalRisk'] >= best_total_risk:
                best_coa = COA['courseOfAction']
                best_total_risk = COA['totalRisk']
    if mission_type == 'defensive':
        for COA in comparative_statics:
            if COA['totalRisk'] <= best_total_risk:
                best_coa = COA['courseOfAction']
                best_total_risk = COA['totalRisk']
    return best_coa


def calculate_units_required(course_of_action):
    units = []
    number_of_personnel = 0
    for task in course_of_action:
        units.append(task['actor'])
    units = list(set(units))
    for unit in units:
        unit_data = get_unit_data(
            unit_id=unit
        )
        if unit_data['affiliation'].upper() == "FRIENDLY":
            number_of_personnel += unit_data['numberOfPersonnel']
    return number_of_personnel

