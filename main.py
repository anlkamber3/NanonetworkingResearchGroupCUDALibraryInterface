import matplotlib.pyplot as plt
import os
import geometry
import domains
import functions

os.chdir('/home/anl/Desktop/nanosim')


#Topology 

### EDIT HERE ONLY
#Distribution Plot
plt.plot(domains.distribution_time_domain, functions.cuda_distribution_plotter("Topology"),label= '$K = Half-Space CUDA Simulation (1cm Reflective Sphere Radius)$')
plt.plot(domains.distribution_time_domain,functions.analytic_distribution(2),label= '$K = Approximation$')

#Cumulative Distribution Plot
#plt.plot(domains.cumulative_distribution_time_domain,functions.cuda_cumulative_distribution_plotter("Topology"),label= '$K = Half-Space CUDA Simulation (1cm Reflective Sphere Radius)$')
#plt.plot(domains.cumulative_distribution_time_domain,functions.analytic_cumulative(2),label= '$K = Approximation$')
### DON'T EDIT BELOW 

print("The phi equals to:" + str(geometry.phi))

plt.legend(loc ="best")
plt.show()

quit()
