import numpy as np

#this is the method of calculating the difference between two consecutive feature values
#Used to make the data stationary
def stationary_differencing(feature):
    first_diffs = feature.values[1:] - feature.values[:-1]
    first_diffs = np.concatenate([first_diffs.flatten(), [0]])
    return first_diffs