import numpy as np


def estimate_quartiles(effect):
    time_data = {
        'DESTROY': [22, 23, 24, 18, 16, 27],
        'DISRUPT': [20, 21, 13, 15, 26, 22],
        'DENY': [11, 12, 13, 6, 9, 13],
        'SEIZE': [11, 12, 15, 16, 13, 17],
        'SECURE': [17, 14, 15, 18, 21, 19],
        'UNDERSTAND': [15, 12, 13, 15, 16, 17],
        'DECEIVE': [14, 16, 13, 14, 15, 16, 18],
        'MOVE': [1, 2, 3, 4, 5, 3, 2, 2, 1]
    }

    time_percentiles = []
    percentiles = [0, 25, 75, 100]
    times = np.array(time_data[effect])
    for p in percentiles:
        time_percentiles.append(np.percentile(times, p))
    return time_percentiles
