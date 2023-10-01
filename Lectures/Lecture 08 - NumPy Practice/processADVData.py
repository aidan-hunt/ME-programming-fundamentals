# -*- coding: utf-8 -*-
"""
Aidan Hunt
4/18/2023
Vectrino Processing

This program processes and visualizes data collected by a Nortek Vectrino
acoustic Doppler velocimeter.
"""

import numpy as np
import matplotlib.pyplot as plt

def importData(dataFile):
    '''
    Given a Vectrino data file, extracts and returns timestamps, beam
    velocities, and beam correlations.

    Parameters
    ----------
    dataFile : str
        Name of the Vectrino .txt file

    Returns
    -------
    timeStamps : numpy array of floats
        Timestamp for each sample, in seconds.
    beamVels : numpy array of floats
        nx4 array of velocity readings, in m/s. Rows represent samples, 
        columns represent each beam.
    beamCorr : numpy array of floats
        nx4 array of beam correlations, in %. Rows represent samples, columns 
        represent each beam.

    '''
    
    # Import full data matrix
    allData = np.loadtxt(dataFile, delimiter=',')
    
    # Extract quantities of interest
    timeStamps = allData[:,0]
    beamVels = allData[:,1:5]
    beamCorr = allData[:,9:] / 255 * 100
    
    return timeStamps, beamVels, beamCorr

def cleanVelocity(timeStamps, beamVel, beamCorr, corrThresh=75):
    '''
    Given Vectrino time stamps, beam velocities, beam correlations, removes
    readings where the correlation on any beam is below a specified threshold,
    and replaces them via linear interpolation of the surrounding points.
    The cleaned velocities are returned.

    Parameters
    ----------
    timeStamps : numpy array of floats
        Timestamp for each sample, in seconds.
    beamVels : numpy array of floats
        nx4 array of velocity readings. Rows represent samples, 
        columns represent each beam.
    beamCorr : numpy array of floats
        nx4 array of beam correlations, in %. Rows represent samples, columns 
        represent each beam.
    corrThresh : float, optional
        Threshold (as a percentage) at and below which readings are replaced via linear
        interpolation. The default is 75.

    Returns
    -------
    cleanVel : numpy array of floats
        nx4 array of velocity readings with "bad" readings replaced, in m/s. 
        Rows represent samples, columns represent each beam. 

    '''
    
    # Identify "bad" readings
    badReading = beamCorr <= corrThresh
    badRows = np.any(badReading, axis=1)
    
    # Preallocate matrix for filtered readings
    cleanVel = np.zeros(beamVel.shape)
    nBeams = beamVel.shape[-1]
    
    for i in range(nBeams): # For each beam of the Vectrino
        # Pull out "good" points to base interpolation on
        goodTime = timeStamps[~badRows]
        goodVel = beamVel[~badRows, i]
        
        # Interpolate all time stamps with good time stamps as basis
        cleanVel[:,i] = np.interp(timeStamps, goodTime, goodVel)
        
    return cleanVel

def coordinateTransform(beamVels, tMat):
    '''
    Converts velocities in beam coordinates to velocities in xyz coordinates

    Parameters
    ----------
    beamVels : numpy array of floats
        nx4 array of velocity readings in beam coordinates. Rows represent
        samples, columns represent each beam.
    tMat : numpy array of floats
       Coordinate transformation matrix for beam to xyz, as a 4x4 matrix.

    Returns
    -------
    numpy array of floats
        nx4 array of velocity readings in xyz coordinates. Rows represent
        samples, columns represent each beam (X, Y, Z1, Z2).

    '''
    xyzVels = tMat @ beamVels.T
    return xyzVels.T

def plotVelocity(time, vel, velFilt, coordInd):
    '''
    Plots a time series of the measured velocity (both filtered and unfiltered)
    in the given coorindate direction

    Parameters
    ----------
    time : numpy vector of floats
        Time stamps of each velocity reading, in seconds
    vel : numpy array of floats
        nx4 array of raw velocity readings in beam coordinates. Rows represent
        samples, columns represent each beam.
    velFilt : numpy array of floats
        nx4 array of filtered velocity readings in beam coordinates. Rows represent
        samples, columns represent each beam.
    coordInd : int
        Integer that represents which coordinate direction to plot:
            0 = X
            1 = Y
            2 = Z1
            3 = Z2

    Returns
    -------
    None.

    '''
    # Generate plot of velocity in given coordinate direction
    plt.figure()
    plt.plot(time, vel[:,coordInd])
    plt.plot(time, velFilt[:,coordInd])
    plt.grid()
    plt.xlabel('Time [s]')
    plt.ylabel('Velocity [m/s]')
    plt.legend(['Unfiltered', 'Filtered'])
    
    # Generate text for title based on coordinate index
    coords = ['X', 'Y', 'Z1', 'Z2']
    plt.title('Velocity in ' + coords[coordInd] + ' direction')
    
#%% Main body of the script
    
# Define data files
dataFile = 'vectrinoData.txt'
transformFile = 'vectrinoTransform.txt'

# Import data from these files
time, beamVel, beamCorr = importData(dataFile)

# Clean velocity time series based on correlation values
beamFilt = cleanVelocity(time, beamVel, beamCorr, corrThresh=75)

# Import transformation matrix and apply coordinate transformation
tMat = np.loadtxt(transformFile, delimiter=',')
vel = coordinateTransform(beamVel, tMat)
velFilt = coordinateTransform(beamFilt, tMat)

# Plot the velocity in a given direction
beamInd = 0
plotVelocity(time, vel, velFilt, beamInd)
