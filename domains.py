import parameters

distribution_time_domain = []
for i in range(int(int(parameters.number_of_steps)/parameters.step_Size)):
    distribution_time_domain.append(i*parameters.time_step*parameters.step_Size)

cumulative_distribution_time_domain = []
for i in range(1,int(int(parameters.number_of_steps))+1):
    cumulative_distribution_time_domain.append(i*parameters.time_step)
