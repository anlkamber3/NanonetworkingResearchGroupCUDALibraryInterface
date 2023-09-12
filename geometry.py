import math
import parameters
r_0_i = math.sqrt(((parameters.location_Of_Spherical_Absorber[0]-parameters.location_Of_Point_Transmitter[0])**2)+((parameters.location_Of_Spherical_Absorber[1]-parameters.location_Of_Point_Transmitter[1])**2)+((parameters.location_Of_Spherical_Absorber[2]-parameters.location_Of_Point_Transmitter[2])**2))

location_Of_Imagine_Spherical_Absorber = (parameters.location_Of_Spherical_Absorber[0]*(-1), parameters.location_Of_Spherical_Absorber[1], parameters.location_Of_Spherical_Absorber[2])
# Imaginer Receiver:

r_j = parameters.r_i
r_0_j = math.sqrt(((location_Of_Imagine_Spherical_Absorber[0]-parameters.location_Of_Point_Transmitter[0])**2)+((location_Of_Imagine_Spherical_Absorber[1]-parameters.location_Of_Point_Transmitter[1])**2)+((location_Of_Imagine_Spherical_Absorber[2]-parameters.location_Of_Point_Transmitter[2])**2))

phi = 0
if ((((2*parameters.location_Of_Spherical_Absorber[0])**2)-(r_0_i**2)-(r_0_j**2))/(-2*r_0_i*r_0_j)) > 1:
    phi = 0
elif ((((2*parameters.location_Of_Spherical_Absorber[0])**2)-(r_0_i**2)-(r_0_j**2))/(-2*r_0_i*r_0_j)) < -1:
    phi = math.pi
else:
    phi = math.acos((((2*parameters.location_Of_Spherical_Absorber[0])**2)-(r_0_i**2)-(r_0_j**2))/(-2*r_0_i*r_0_j))


r_0_ij = math.sqrt(((r_0_j-(r_j*(r_j/r_0_j)))**(2))+(r_0_i**(2))-(2*r_0_i*math.cos(phi)*(r_0_j-(r_j*(r_j/r_0_j)))))

r_0_ji = math.sqrt(((r_0_i-(parameters.r_i*(parameters.r_i/r_0_i)))**(2))+(r_0_j**(2))-(2*r_0_j*math.cos(phi)*(r_0_i-(parameters.r_i*(parameters.r_i/r_0_i)))))
