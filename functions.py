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


def analytic_distribution(communication_system):
    datas = []
    for i in range(1, int(parameters.number_of_steps)):
        datas.append((analytic_formulation((i+1)*parameters.time_step, communication_system)-analytic_formulation(i*parameters.time_step, communication_system))*parameters.total_molecules)
    scaled_datas = []
    for i in range(int(parameters.number_of_steps/parameters.step_Size)):
        scaled_datas.append(sum(datas[i*parameters.step_Size:(i+1)*parameters.step_Size]))
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


def cuda_distribution_plotter(filename):

    zero_array = np.zeros(int(parameters.number_of_steps))

    for i in range(parameters.number_of_simulations):
        sim_datas = opener(i, filename)
        for x in sim_datas:
            zero_array[x-1] += 1

    zero_array = zero_array / parameters.number_of_simulations
    output = []

    for i in range(int(parameters.number_of_steps/parameters.step_Size)):
        output.append(sum(zero_array[(i*parameters.step_Size):((i+1)*parameters.step_Size)]))

    return output


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
