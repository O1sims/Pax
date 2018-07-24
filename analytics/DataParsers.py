def c2_data_parser(expected, data, root="Root"):
    """
    Returns all the expected keys that are missing from the data.
    Does not handle two dimensional lists.
    :param expected:
    :param data:
    :param root:
    :return:
    """
    if not isinstance(data, dict):
        return None

    expected_set = set(expected.keys())
    data_set = set(data.keys())

    missing_keys = expected_set - data_set
    result = {}

    for key in expected_set.intersection(data_set):
        # Are we dealing with a list type?
        if key in data and isinstance(data[key], list):
            for count in range(0, len(data[key])):
                # Check if there are missing keys in the list
                child_result = c2_data_parser(expected[key][0], data[key][count], key + "_index_" + str(count))

                if child_result:
                    if key not in result:
                        result[key] = []
                    result[key].append(child_result)

        # Are dealing with a dict type?
        if isinstance(data[key], dict):
                child_result = (c2_data_parser(expected[key], data[key], key))
                if child_result:
                    result[key] = child_result

    result_set = {root: list(missing_keys)}

    # Check if the children had a missing keys
    if len(result) > 0:
        result_set[root].append(result)

    if len(result_set[root]) > 0:
        return result_set

    return None

