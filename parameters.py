# Parameters

# All the units of parameters are SI units.

D = 79.4*(10**-12)

total_molecules = 10**6

time_step = 10**(-4)  # Time Resolution

t = 2  # Simulation Run Time

number_of_steps = t/time_step

step_Size = 50  # Scaling when plotting the distribution.

number_of_simulations = 400

maximum_distance = 30

symbol_duration_multiplier = 5
# Half Space Analytic(It is assumed that reflective wall is always yz plane.)

location_Of_Point_Transmitter = (0, 0, (10**(-5)))
location_Of_Spherical_Absorber = ((10**(-5)), 0, 0)

# Receiver:

r_i = 5*(10**(-6))

