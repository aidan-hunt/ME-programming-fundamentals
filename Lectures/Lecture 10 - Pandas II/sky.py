# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:18:01 2023

@author: Aidan Hunt
"""

import numpy as np
import pandas as pd

def importUSGSData(fileName, metricName):
    '''
    Reads a USGS .txt file given by fileName (as a string) and returns 
    the result as a dataframe. The 5th column is labeled using the 
    given metricName (as a string).
    '''
    
    # Import data, keeping only the columns that we are interested in
    colNames = ['Timestamp', metricName]
    df = pd.read_csv(fileName, skiprows=29, delimiter='\t', 
                 header=None, usecols=[2, 4], names=colNames)
    
    # Convert timestamps to datetime and set as index
    df.set_index('Timestamp', inplace=True)
    df.index = pd.to_datetime(df.index)
    
    # Return object
    return df

skyFlow = importUSGSData('sky_flow.txt', 'flow')
skyTemp = importUSGSData('sky_waterTemp.txt', 'temp')
skyHeight = importUSGSData('sky_height.txt', 'height')

#%% Merge
sky = pd.concat([skyFlow, skyHeight, skyTemp], axis=1)
# sky2 = pd.merge(skyFlow, skyTemp, how='outer', left_index=True, right_index=True)