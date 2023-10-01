# -*- coding: utf-8 -*-
"""
Aidan Hunt

This program calculates the voltages on a series circuit with resistors. 
The user is prompted for the supply voltage and resistances in the circuit.
The total current and voltages across each resistor are calculated and printed.

(Basic operations)
"""

# Print welcome message
print('Welcome to the resistor voltage calculator.')
print()

# Get input voltage from user
vSupply = float(input('Please enter the supply voltage (V): '))

# Get number of resistances from user
nRes = int(input('Please enter the number of resistors: '))

# Get values of resistances from user
resOhms = [None] * nRes
totalRes = 0
for i in range(nRes):
    promptStr = 'Please enter the resistance (ohms) for resistor #' + str(i+1) + ': '
    currOhms = float(input(promptStr))
    
    # Add to list and total 
    resOhms[i] = currOhms
    totalRes += currOhms
    
# Calculate current
I = vSupply / totalRes

# Calculate voltage across each resistor
resVolts = [ohms * I for ohms in resOhms]

# Print a summary of the results
print()
print('Supply voltage (V):', vSupply)
print('Current (A):', I)
print('Resistances (ohms):', resOhms)
print('Voltage across each resistor (V):', resVolts)