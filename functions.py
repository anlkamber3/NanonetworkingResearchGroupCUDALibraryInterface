import math
import numpy as np
import parameters
import geometry
import domains

# Functions that are needed to analytical formulations


def analytic_formulation(t, communication_system):

    if communication_system == 0:
        return (parameters.r_i/geometry.r_0_i)*math.erfc((geometry.r_0_i-parameters.r_i)/math.sqrt(4*parameters.D*t))

    elif communication_system == 1:
        return (parameters.r_i/geometry.r_0_i)*math.erfc((geometry.r_0_i-parameters.r_i)/math.sqrt(4*parameters.D*t))-(((geometry.r_j*parameters.r_i)/(geometry.r_0_j*geometry.r_0_ij))*math.erfc((((geometry.r_0_i+geometry.r_0_ij)-(parameters.r_i+geometry.r_j))/math.sqrt(4*parameters.D*t))))

    elif communication_system == 2:
        return ((parameters.r_i/geometry.r_0_i)*math.erfc((geometry.r_0_i-parameters.r_i)/math.sqrt(4*parameters.D*t))-(((geometry.r_j*parameters.r_i)/(geometry.r_0_j*geometry.r_0_ij))*math.erfc((((geometry.r_0_i+geometry.r_0_ij)-(parameters.r_i+geometry.r_j))/math.sqrt(4*parameters.D*t)))))+((geometry.r_j/geometry.r_0_j)*math.erfc((geometry.r_0_j-geometry.r_j)/math.sqrt(4*parameters.D*t))-(((geometry.r_j*parameters.r_i)/(geometry.r_0_i*geometry.r_0_ji))*math.erfc((((geometry.r_0_j+geometry.r_0_ji)-(parameters.r_i+geometry.r_j))/math.sqrt(4*parameters.D*t)))))


def analytic_distribution(communication_system,step_size):
    datas = []
    for i in range(1, int(parameters.number_of_steps)):
        datas.append((analytic_formulation((i+1)*parameters.time_step, communication_system)-analytic_formulation(i*parameters.time_step, communication_system))*parameters.total_molecules)
    scaled_datas = []
    for i in range(int(parameters.number_of_steps/step_size)):
        scaled_datas.append(sum(datas[i*step_size:(i+1)*step_size]))
    return scaled_datas


def analytic_cumulative(communication_system):
    datas = []
    for i in domains.cumulative_distribution_time_domain:
        datas.append(analytic_formulation(i, communication_system)*parameters.total_molecules)
    return datas


# CUDA Simulation
def opener(i, filename):

    sim_datas_new = []

    with open(f"{filename}{i}", "r") as file:
        for line in file:
            concurrent_list = line.rstrip().split(" ")
            sim_datas_new.append(int(concurrent_list[3]))

    return sim_datas_new


def cuda_distribution_plotter(filename,step_size):

    zero_array = np.zeros(int(parameters.number_of_steps))

    for i in range(parameters.number_of_simulations):
        sim_datas = opener(i, filename)
        for x in sim_datas:
            zero_array[x-1] += 1

    zero_array = zero_array / parameters.number_of_simulations
    output = []

    for i in range(int(parameters.number_of_steps/step_size)):
        output.append(sum(zero_array[(i*step_size):((i+1)*step_size)]))

    return output


def cuda_distribution_plotter_sir(filename,i):

    zero_array = np.zeros(int(parameters.number_of_steps))
    zero_array = list(zero_array)
    sim_datas = opener(i,filename)

    for x in sim_datas:
        zero_array[x-1] += 1
    index = zero_array.index(max(zero_array))
    return index, zero_array

def signal_to_interference_ratio(index,array,symbol_duration_multiplier):
    buffer = []
    for i in range(len(array)):
        if i == 0:
            buffer.append(array[i])
        else:
            buffer.append((array[i]+buffer[i-1]))
    return ((buffer[index*symbol_duration_multiplier]) / (buffer[-1]-buffer[index*symbol_duration_multiplier]))*100,
def cuda_cumulative_distribution_plotter(filename):

    zero_array = np.zeros(int(parameters.number_of_steps))

    for i in range(parameters.number_of_simulations):
        sim_datas = opener(i, filename)
        for x in sim_datas:
            zero_array[x-1] += 1

    zero_array = zero_array / parameters.number_of_simulations

    buffer = []

    for i in range(len(zero_array)):
        if i == 0:
            buffer.append(zero_array[i])
        else:
            buffer.append((zero_array[i]+buffer[i-1]))

    return buffer


def find_maximum(filename):
    data = cuda_distribution_plotter(filename,1)
    index = data.index(max(data))
    print(index)
    return index


def signal_to_noise_ratio(filename):
    index = find_maximum(filename)*5
    data = cuda_cumulative_distribution_plotter(filename)
    return ((data[index]) / (data[-1]-data[index]))*100, data[-1]
