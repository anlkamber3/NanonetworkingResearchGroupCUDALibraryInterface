# This script runs simulations. You can adjust the number of them and the names.

import os
import parameters


largest_x = 5


def code(location):
    return ['#include <nanosim/simulation.h>\n', '#include <nanosim/sphere.h>\n', '#include <nanosim/periodic_transmitter.h>\n', '#include <nanosim/obstacle_group.h>\n', '#include <nanosim/aarectangularprism.h>\n', '#include <iostream>\n', '#include <string>\n', '\n', 'using namespace std;\n', 'using namespace nanosim;\n', '\n', 'SimulationResult benchmark()\n', '{\n', '\tNoFlowEnvironment env(1e-4, 79.4e-12);\n', '\tconst unsigned particle_count = 1000000;\n', '\n', '\tPeriodicTransmitter transmitter(\n', '\t\tPoint(2*(1e-5), 0, 0),\n', '\t\tparticle_count\n', '\t);\n', '\n', '\tReceivingAbsorbentSphere receiver(0, 5e-6,Point((1e-5),0,0));\n', '\t\n', f'\tNonReceivingReflectiveAARectangularPrism reflective_prism(1, {location});\n', '\n', '\tauto sim = createSimulation(env, createObstacleGroup(receiver, reflective_prism), transmitter, particle_count);\n', '\n', '\treturn sim.run(2);\n', '}\n', '\n', 'int main()\n', '{\n', '\tSimulationResult res = benchmark();\n', '\n', '\tconst auto& receptions = *res.receptions;\n', '\n', '\tfor (int i=0; i<receptions.size(); i++)\n', '\t{\n', '\t\tReceptionRecord r = receptions[i];\n', '\t\tprintf("%f %f %f %d 0\\n", r.p.pos.x*1e6, r.p.pos.y*1e6, r.p.pos.z*1e6, r.timestep);\n', '\t}\n', '\treturn 0;\n', '}']


def location(largest_x):
    return "{"+"{"+f"{largest_x-4}e-6, -20e-6, -20e-6"+"}"+","+ "{"+f"{largest_x}e-6, 20e-6, 20e-6"+"}"+"}"


for distance in range(0,parameters.maximum_distance+1):
    os.chdir('/home/anl/Desktop/nanosim/scenarios/benchmark')
    file = os.open("main.cu",os.O_RDWR|os.O_CREAT)
    file_output = os.fdopen(file,"w")
    file_output.writelines(code(location(largest_x)))
    file_output.close()

    os.chdir('/home/anl/Desktop/nanosim')

    os.system('cmake .')
    os.system('make')
    for i in range(parameters.number_of_simulations):
        os.system(f'./sim_benchmark.exe > {parameters.name_of_simulation}{distance}{"-"}{i}')

    largest_x -= 1


quit()



