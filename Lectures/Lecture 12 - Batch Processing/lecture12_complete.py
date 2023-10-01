# -*- coding: utf-8 -*-
"""
Aidan Hunt
5/2/2023

Lecture 12 - Batch Processing
"""

# Goal: determine, for each torque cell, the voltage
# to torque conversion factor based on the collected data

# Consider how we should scale our code to handle more than one torque cell

import os, glob # These are helpful for working with files
import numpy as np # Use to import data, create arrays
import matplotlib.pyplot as plt # For creating plots
plt.rcParams['figure.dpi'] = 199

# Define our cell IDs
cellIDs = ['3C', '3B']

# Everything below here stays the same, no matter how many torque cells we have
def getTorqueCellCalibration(cellIDs):
    '''
    Given a list of torque cell IDs, finds files that match each torque cell
    ID in the 'Torque Cell Data' folder in the current working directory, with
    the naming convention 'torqueCell_ID_MMMg.txt', where ID is the torque cell
    ID and MMM is a three digit number that represents the mass, in grams, used
    in the calibration.
    Finds the voltage to torque conversion factor for each cell based on the
    voltage data provided. Returns the conversion factor for each slope.
    Also generates a plot showing the voltage vs torque relationship for each
    cell, and the corresponding line of best fit.
    '''
    
    convSlope = np.zeros(len(cellIDs))
    
    # Create plot
    plt.figure()
    
    for cellIndex, currCell in enumerate(cellIDs):
    
        # Find potential files based on the current cell ID
        fileFormat = os.path.join('.', 'Torque Cell Data', currCell, 'torqueCell_' + currCell + '_*g.txt')   # Use os to create a file format
        fileList = glob.glob(fileFormat)
        print(fileFormat)
            
        # Aggregate our data across all files in arrays
        voltages = np.zeros(len(fileList)) # Preallocate an array for voltages
        mass = np.zeros(len(fileList)) # Preallocate an array for the masses
        
        for i, currFile in enumerate(fileList): # For each file
            # Load the file with numpy
            currData = np.loadtxt(currFile)
            
            # Voltage is in the text data (mean of data)
            voltages[i] = np.mean(currData)
            
            # Mass info is in the file name
            currFile = currFile.replace('g.txt', '')
            currMass = float(currFile[-3:])
            mass[i] = currMass  
            # print(currFile)
            # print(currMass)
            
        # Convert masses to torques
        g = 9.81 # Acceleration due to gravity [m/s^2]
        L = 20.85/100 # Lever arm [m]
        F = mass / 1000 * g # Force = Mass x gravity
        torque = F * L    # Torque = Force x Distance
        
        # Determine conversion factor via line of best fit
        polyCoeff = np.polyfit(voltages, torque, deg=1)
        torqueFit = np.polyval(polyCoeff, voltages)
        convSlope[cellIndex] = polyCoeff[0]
        
        # Plot the current data
        plt.scatter(voltages, torque, label=currCell)
        plt.plot(voltages, torqueFit, '--k')
        
    # Format
    plt.grid()
    plt.xlabel('Voltage [V]')
    plt.ylabel('Torque [N-m]')
    plt.legend()
    
    # Return the conversion slope
    return convSlope
    
getTorqueCellCalibration(cellIDs)