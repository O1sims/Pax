

def generate_course_action_breadth(root_task, tasks):
    copy_data = [root_task["taskId"]]
    data = process_task_list_breadth(tasks, copy_data)

    clean_data = remove_replicated_task(data)

    return clean_data[::-1]

def generate_course_action_depth(root_task, tasks):

    data = process_task_list_depth(tasks, [root_task["taskId"]])
    clean_data = remove_replicated_task(data)

    return clean_data[::-1]


def process_task_list_breadth(tasks, current_list):

    process_list = []

    for element in current_list:

        target_task = filter(lambda task: task["taskId"] == element, tasks)[0]["dependencies"]
        process_list += target_task

    if len(process_list) > 0:

        current_list += process_task_list_breadth(tasks, process_list)
        return current_list

    return current_list

def process_task_list_depth(tasks, current_list):

    process_list = []

    for element in current_list:

        target_task = filter(lambda task: task["taskId"] == element, tasks)[0]["dependencies"]

        for t in target_task:

            process_list += process_task_list_depth(tasks, [t])

    current_list += process_list

    return current_list

def extract_tasks(task_list, tasks):

    export_list = []

    for t in task_list:

        export_list += filter(lambda task: task["taskId"] == t, tasks)

    return export_list

def remove_replicated_task(task_list):

    seen = {}
    new_list = []
    position = 0

    for t in task_list:

        if t not in seen:
            new_list.append(t)
            seen[t] = position
        else:
            del new_list[seen[t]] # move the dependency down the list
            position -= 1
            seen[t] = position
            new_list.append(t)

        position += 1


    return new_list