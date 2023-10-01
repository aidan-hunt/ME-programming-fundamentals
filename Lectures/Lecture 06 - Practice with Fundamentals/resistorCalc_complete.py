# -*- coding: utf-8 -*-
"""
Aidan Hunt

This program calculates the voltages on a series circuit with resistors. 
The user is prompted for the supply voltage and resistances in the circuit.
The total current and voltages across each resistor are calculated and printed.

(Basic operations, factored into functions, plus error handling)1
"""

#%% Define subfunctions
def printStartup():
    '''
    Prints the startup message for the resistor calculator.
    '''
    print('Welcome to the resistor voltage calculator.')
    print()

# Get input voltage
def getSupplyVoltage():
    '''
    Prompts the user for the supply voltage and returns the input as a float.
    '''
    
    vSupply = input('Please enter the supply voltage (V): ')
    return float(vSupply)

# Determine resistances
def getNumberOfResistors():
    '''
    Prompts the user for the number of resistors in the circuit and returns
    the result as an int.
    '''
    
    nRes = input('Please enter the number of resistors: ')
    return int(nRes)

def getResistances(nRes):
    '''
    Given the number of resistors in a series circuit, prompts the user for the
    resistance in ohms of each resistor. Returns the resistances (as a list of
    floats), as well as the total resistance in the circuit (as a float)
    
    If the user enters a resistance less than or equal to zero for any
    resistor, they are prompted again until they enter a positive value.
    '''
    
    resOhms = [None] * nRes
    totalRes = 0
    for i in range(nRes):
        promptStr = 'Please enter the resistance (ohms) for resistor #' + str(i+1) + ': '
        currOhms = float(input(promptStr))
        
        while currOhms <= 0:
            currOhms = float(input(promptStr))
        
        # Add to list and total 
        resOhms[i] = currOhms
        totalRes += currOhms
        
    return resOhms, totalRes
    
# Calculate current
def calcCurrent(vSupply, totalRes):
    '''
    Given the supply voltage (V) and total resistance (ohms) in a series circuit,
    calculates and returns the current in the circuit (in Amperes). All inputs
    and outputs are assumed to be floats.
    '''
    
    I = vSupply / totalRes
    return I

# Calculate voltage across each resistor
def calcResistorVoltages(resOhms, I):
    '''
    Given a list of resistances (as a float, in Ohms) and total current 
    (as a float, in Amperes) in a series circuit, calculates the 
    voltage drop across each resistor. The result is returned as a list of floats.
    '''
    
    resVolts = [ohms * I for ohms in resOhms]
    return resVolts

# Print a summary of the results
def printSummary(vSupply, I, resOhms, resVolts):
    '''
    Given the supply voltage of a series circui (in Volts), the current in the
    circuit (in Amps), a list of the resistances in the circuit (in ohms), 
    and a list of the voltages across each resistor (in Volts), prints a 
    summary of the circuit properties to the console.
    '''
    print()
    print('Supply voltage (V):', vSupply)
    print('Current (A):', I)
    print('Resistances (ohms):', resOhms)
    print('Voltage across each resistor (V):', resVolts)
    
#%% Main body of script
'''
Prompts the user for properties of a series circuit. Computes the current in
the circuit as a function of the specified resistances, as well as the
voltage drop across each resistor. Prints a summary to the console.

If the user specifies an invalid number of resistors (less than or equal
to zero), no calculation is performed.
'''

# Print welcome message
printStartup()

# Get input voltage and number of resistors
vSupply = getSupplyVoltage()
nRes = getNumberOfResistors()

# Choose what to do best on the number of resistors
if nRes < 0: #  A negative number of resistors was specified
    print('Invalid number of resistors - no calculation performed.')
elif nRes == 0: # Zero resistors specified
    print('No resistors specified - short circuit!')
else: # A positive number of resistors specified
    # Calculate resistances
    resOhms, totalRes = getResistances(nRes)
    
    # Calculate current and resistor voltages
    I = calcCurrent(vSupply, totalRes)
    resVolts = calcResistorVoltages(resOhms, I)
    
    # Print results
    printSummary(vSupply, I, resOhms, resVolts)