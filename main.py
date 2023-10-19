import matplotlib.pyplot as plt
import os
import parameters
import geometry
import functions
import numpy as np
os.chdir('/home/anl/Desktop/nanosim')


SIR_matrix = np.zeros((parameters.maximum_distance+1,parameters.number_of_simulations))
for i in range(0,parameters.maximum_distance+1):
    filename = f"{parameters.name_of_simulation}{i}-"
    for simulation_number in range(parameters.number_of_simulations):
        index, array = functions.cuda_distribution_plotter_sir(filename, simulation_number)
        SIR = functions.signal_to_interference_ratio(index, array,parameters.symbol_duration_multiplier)
        SIR_matrix[i,simulation_number] = SIR[0]
np.savetxt(f"/home/anl/PycharmProjects/pythonProject/NEW/signaltointerferenceratio{parameters.symbol_duration_multiplier}.txt", SIR_matrix)

#Cumulative Distribution Plot
#plt.plot(domains.cumulative_distribution_time_domain,functions.cuda_cumulative_distribution_plotter("topology_zero"),label= '$K = Half-Space CUDA Simulation (1cm Reflective Sphere Radius)$')
#plt.plot(domains.cumulative_distribution_time_domain,functions.analytic_cumulative(2),label= '$K = Approximation$')


print("The phi equals to:" + str(geometry.phi))


plt.show()

quit()
