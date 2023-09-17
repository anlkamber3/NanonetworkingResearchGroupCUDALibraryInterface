# NanonetworkingResearchGroupCUDALibraryInterface
It is a simple user interface to utilize GPU Simulation Library of Boğaziçi Nanonetworking Research Group in Ubuntu.


The interface was designed to utilize the CUDA GPU Accelerated Library of Boğaziçi
Nanonetworking Research Group. The user interface offers an ease of use in case the users are not
familiar with the Linux environment. In one click, the user is able to run hundreds of simulations of
molecular communication via diffusion systems, and is enabled to take average of the simulation results to
eliminate white Gaussian noise. Also, the user can plot the simulation results and analytical
formulations.


First, download the CUDA Library to desktop. If you want to download it to another path, edit the line,

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
