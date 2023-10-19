import numpy as np
import parameters
import matplotlib.pyplot as plt
matrix= np.zeros((parameters.maximum_distance+1,parameters.number_of_simulations))
i=0
with open(f"signaltointerferenceratio{parameters.symbol_duration_multiplier}.txt", "r") as file:
    for line in file:
        concurrent_list = line.rstrip().split(" ")
        concurrent_list = np.array(concurrent_list)
        matrix[i,:] = concurrent_list
        i += 1


means = np.sum(matrix,axis = 1)
means = means / (matrix.shape[1])
plt.plot(means)
plt.ylim(100,140)
plt.xlabel("distance (micron)")
plt.ylabel("Signal to Interference Ratio (%)")
plt.grid()
plt.show()
