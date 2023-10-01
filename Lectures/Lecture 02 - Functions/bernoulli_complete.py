"""
Aidan Hunt
3/28/2023

This program calculates downstream pressure in a pipe using the Bernoulli 
equation and known fluid properties. It demonstrates several ways of calling
functions with optional input parameters.
"""

#%% Define basic functions

def calcHydrostaticPressure(z, rho, g):
    '''
    Given an elevation (z), density (rho), and acceleration due to gravity (g),
    calculates and returns the hydrostatic pressure term from the
    Bernoulli equation. All inputs are assumed to be numeric and have compatible
    units.
    '''
    return z*rho*g

def calcDynamicPressure(V, rho):
    '''
    Given a velocity (V) and density (rho), calculates and returns the 
    dynamic pressure term from the Bernoulli equation. All inputs are assumed 
    to be numeric and have compatible units.
    '''
    return 1/2*rho*V**2


#%% Define Bernoulli function for finding pressure at a downstream location
def calculateDownstreamPressure(P1, V1, V2, z1, z2, rho=1000, g=9.81):
    '''
    Given known upstream and downstream fluid properties, as well as the density
    and acceleration due to gravity, calculates and returns the downstream pressure.
    All inputs are assumed to be numeric.
    
    Required Inputs:
        P1 - upstream pressure in Pa
        V1 - upstream velocity in m/s
        V2 - downstream velocity in m/s
        z1 - upstream elevation in m
        z2 - downstream elevation in m
        
    Optional Inputs:
        rho - fluid density in kg/m^3 (default 1000)
        g - acceleration due to gravity in m/s^2 (default 9.81)
        
    Ouptuts
        The downstream pressure, P2, in Pa
    '''
    
    # Calculate difference between upstream and downstream hydrodynamic terms
    deltaHydrostatic = calcDynamicPressure(V1, rho) - calcDynamicPressure(V2, rho)
    
    # Calculate difference between upstream and downstream dynamic terms
    deltaDynamic = calcHydrostaticPressure(z1, rho, g) - calcHydrostaticPressure(z2, rho, g)
    
    # Calculate downstream pressure and return
    P2 = P1 + deltaHydrostatic + deltaDynamic
    
    return P2


#%% Perform computation(s) of interest

# Specify fluid properties
rho = 850
g = 9.81
Patm = 101.325 * 10**3 # Atmospheric pressure

# Specify upstream properties
P1 = 10 * Patm
V1 = 3
z1 = 5

# Specify known downstream properties
V2 = 5
z2 = 0
# P2 unknown

# Get downstream pressure (using default rho and g)
P2 = calculateDownstreamPressure(P1, V1, V2, z1, z2)
print(P2)

# Get downstream pressure (using default g and rho=850)
rhoNew = 850
P2 = calculateDownstreamPressure(P1, V1, V2, z1, z2, rhoNew)
print(P2)

# Get downstream pressure (using different rho and g)
gNew = 100
rhoNew = 850
P2 = calculateDownstreamPressure(P1, V1, V2, z1, z2, rhoNew, gNew) 
print(P2)

# Same as above, but passing in rho and g out of order
gNew = 100
rhoNew = 850
P2 = calculateDownstreamPressure(P1, V1, V2, z1, z2, g=gNew, rho=rhoNew) 
print(P2)
    
