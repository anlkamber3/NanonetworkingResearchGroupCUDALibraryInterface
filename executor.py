# This script runs simulations. You can adjust the number of the simulations and the names of the text files.

import os

name_of_simulation = "Topology"

number_of_simulations = 100

os.chdir('/home/anl/Desktop/nanosim') #It is the path of the location of CUDA Library

os.system('cmake .')

os.system('make')

for i in range(number_of_simulations):
    os.system(f'./sim_benchmark.exe > {name_of_simulation}{i}')

#You can visualize one of the simulation results to see how simulation works.

#simulation_To_Visualize = "Topology1"

#os.system(f'./visualize.py {simulation_To_Visualize}')

quit()



