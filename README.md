# NanonetworkingResearchGroupCUDALibraryInterface
It is a simple user interface to utilize GPU Simulation Library of Boğaziçi Nanonetworking Research Group in Ubuntu

This interface enables user to simulate different topologies of molecular communication systems by executing CUDA Library of Nanonetworking Research Group. What this interface offers is that you can easily simulate a topology a number of times without using Linux console

The interface compares simulation results with the analytical formulation of three dimensional half space characteristics of molecular communication via diffusion channel with an absorbing spherical receiver. However, it can be used to read simulation results of the any kind of environment. The interface is easy to use. First, download the CUDA Library to desktop. If you want to download it to another path, change the line , which is

```
os.chdir(f'/home/{username}/Desktop/nanosim')
```
You can change the number of simulations that you want to execute and the name of the text files. In each iteration, executor.py adds the index of the for loop to the end of the name of the text file. 

```
name_of_simulation = "Topology"

number_of_simulations = 100
```

When you run the executor.py, the simulation process begins. It runs simulation number_of_simulations times. 

Then check whether the parameters in parameters.py match well with the parameters in the library.

```
D = 79.4*(10**-12)

total_molecules = 10**6

time_step = 10**(-4)  # Time Resolution

t = 2  # Simulation Run Time

number_of_steps = t/time_step

step_Size = 50  # Scaling when plotting the distribution.

number_of_simulations = 100

location_Of_Point_Transmitter = (0, 0, (10**(-5)))
location_Of_Spherical_Absorber = ((10**(-5)), 0, 0)
```

Then you can run,
```
plt.plot(domains.distribution_time_domain, functions.cuda_distribution_plotter("Topology"))
```
if you are plotting molecule distribution function on absorbing receiver or absorbing receivers.

If you are plotting cumulative molecule distribution function on absorbing receiver or absorbing receivers, then

```
plt.plot(domains.cumulative_distribution_time_domain,functions.cuda_cumulative_distribution_plotter("Topology"))
```

Have a good time :) 
