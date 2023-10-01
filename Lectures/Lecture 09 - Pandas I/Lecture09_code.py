# -*- coding: utf-8 -*-
"""
Aidan Hunt
4/24/2023

Lecture 09 and 10 - Live
"""

# Import packages
import pandas as pd
import numpy as np

#%% Example of importing a data file
fileName = 'sky_flow.txt'

# skiprows: specify how many rows to skip before reading data
# delimiter: specify how column entries are separated
# names: specify column names directly
colNames = ['Agency', 'Site', 'Timestamp', 'Timezone', 'Flow', 'Approval']
skyFlow = pd.read_csv(fileName, skiprows=29, delimiter='\t', names=colNames)

# Set our index to be our timestamps
# inplace=True modifies the existing DataFrame, rather than returning a new one
skyFlow.set_index('Timestamp', inplace=True)

#%% Indexing

# Use .loc to reference by row/column names
locEx1 = skyFlow.loc['2021-12-31 23:45'] # Extract row corresponding to this timestamp

# Slicing works too!
# Get rows from 12/31/2021 at 23:45 to 3/1/2022 at 00:00, as well as 
# columns from Site to Flow
locEx2 = skyFlow.loc['2021-12-31 23:45':'2022-03-01 00:00', 'Site':'Flow'] 

# Use iloc to index based on row or column number (e.g., first 5 rows, 3rd column)
# Uses "implicit" index
ilocEx = skyFlow.iloc[0:5, 2]

# Use logical indexing to extract rows that meet a particular condition
logicEx = skyFlow.loc[skyFlow.Flow > 6000] # Get rows with flows above 6000 cfs

#%% Convert our index to a datetime

skyFlow.index = pd.to_datetime(skyFlow.index)

# Now we can very conveniently index based on year, year-month, etc
dataFrom2021 = skyFlow.loc['2021']

dataFromMarch2021 = skyFlow.loc['2021-3']

years = skyFlow.index.year

#%% Pseudocode outline - finding monthly averages and months of largest discharge

# Get the years that we want to consider
years = skyFlow.index.year
years = np.unique(years)

# Get the months that we want to consider
months = np.unique(skyFlow.index.month)

# Preallocating storage for monthly averages
monthlyAverages = np.zeros([len(years), len(months)])

# For each year
for i, currentYear in enumerate(years):
    for j, currentMonth in enumerate(months):
        # Build some sort of indexing string based on the month and year
        monthYear = str(currentYear) + '-' + str(currentMonth)
        
        # Slice the DataFrame at that year
        currSlice = skyFlow.loc[monthYear] 
        
        # Find and store the average of that month/year
        monthlyAverages[i,j] = np.mean(currSlice.Flow)

# Convert the data matrix of monthly averages into the vector that we want

# Use np.argmax to find the index of each maximum in each row
maxMonthInd = np.argmax(monthlyAverages, axis=1) # axis=1 "along columns"
maxMonths = maxMonthInd + 1




