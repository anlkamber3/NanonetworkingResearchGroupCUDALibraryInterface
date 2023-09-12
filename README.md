# NanonetworkingResearchGroupCUDALibraryInterface
It is a basic user interface to use Nanonetworking GPU Simulation Library in Ubuntu

This interface provides an easy way to simulate different topologies of molecular communication via diffusion systems by executing CUDA Libary of Nanonetworking Research Group. What this interface offers is that you can easily simulate a topology a number of times without using Linux console, and plot molecule distribution function on absorbing receiver against time.

The interface is built for comparing simulation results and analytical formulation for three dimensional half space characteristics of molecular communication via diffusion channel with an absorbing spherical receiver. However, it can be used for reading simulation results of any kind of environment. The way you can use it is simple. First download the CUDA Library to Desktop. If you want to download it to another path, change the line 

```
os.chdir(f'/home/{username}/Desktop/nanosim')
```
You can change the number of simulations that you want to execute and the name of the text files. In each iteration, executor.py adds the index of the for loop to the end of the name of the text file. 

```
name_of_simulation = "Topology"

number_of_simulations = 100
```

When you run the executor.py, the simulation process begins. It runs number_of_simulations time simulations. 

Then check whether the parameters in parameters.py match well with the parameters in the library.

```
D = 79.4*(10**-12)

total_molecules = 10**6

time_step = 10**(-4)  # Time Resolution

t = 2  # Simulation Run Time

number_of_steps = t/time_step

step_Size = 50  # Scaling when plotting the distribution.

number_of_simulations = 100

# Half Space Analytic(It is assumed that reflective wall is always yz plane.)

location_Of_Point_Transmitter = (0, 0, (10**(-5)))
location_Of_Spherical_Absorber = ((10**(-5)), 0, 0)
```

Then you can run,
```
plt.plot(domains.distribution_time_domain, functions.cuda_distribution_plotter("Topology"))
```
if you are plotting molecule distribution function on absorbing receiver.

If you are plotting cumulative molecule distribution function on absorbing receiver, then

```
plt.plot(domains.cumulative_distribution_time_domain,functions.cuda_cumulative_distribution_plotter("Topology"))
```
