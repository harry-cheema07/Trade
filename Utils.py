import numpy as np
import matplotlib.pyplot as plt


#this is the method of calculating the difference between two consecutive feature values
#Used to make the data stationary
def stationary_differencing(feature):
    first_diffs = feature.values[1:] - feature.values[:-1]
    first_diffs = np.concatenate([first_diffs.flatten(), [0]])
    return first_diffs

#This method can be used to check the stationarity in dataset
#It is expecting diff column to be present in the dataframe to plot the graph
def plotStationarity(feature):
    plt.figure(figsize=(12,6))
    plt.plot(feature['diff'])
    plt.axhline(0, linewidth=1, color='black')
    return plt.show()