# -*- coding: utf-8 -*-
"""
Aidan Hunt
5/17/2023

Lecture 16 - Live
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Add UW colors and create custom colormap
uwPurple = '#4b2e83'
uwGold = '#b7a57a'
uwMap = colors.LinearSegmentedColormap.from_list('goDawgs', [uwPurple, 'white', uwGold])

plt.rcParams['figure.dpi'] = 199 # For Aidan's computer

# Import our data
rawTxt = np.loadtxt('freeSurface.txt', delimiter=',')
nSweeps = rawTxt.shape[1]

# Reshape our data
fstData = np.reshape(rawTxt, [7, 22, nSweeps], order='F')

# Create our grid
D = 31.5 # cm
w = 76 # cm
dx = D/6
dy = w/8
x = np.arange(D/2, 4*D + dx, dx)
y = np.arange(-w/2+dy, w/2, dy)

X, Y = np.meshgrid(x, y)

# We want to create a figure with 4 subplots (1 row, 4 columns)
    # Use sharex and sharey
    # Constrained layout
fig, ax = plt.subplots(nrows=1, ncols=nSweeps,
                       sharex=True, sharey=True,
                       layout='constrained',
                       figsize=[10,3])

# Want to plot each slice
for i in range(nSweeps):
    
    # Color data is "main piece"
    mesh = ax[i].pcolormesh(X, Y, fstData[:,:,i], 
                     vmin=np.min(fstData), vmax=np.max(fstData),
                     shading='gouraud',
                     cmap=uwMap) # Specify colormap here
    
    # Scatter plot of locations
    ax[i].scatter(X, Y, c='black', s=4)
    
    # Add xlabels and title
    ax[i].set_xlabel('x [cm]')
    ax[i].set_title('Sweep ' + str(i+1))
    
    # Set ticks of each plot
    xtickVals = np.arange(0, 4*D+D/2, D/2)
    ytickVals = np.arange(-w/2, w/2+w/4, w/4)
    
    ax[i].set_xticks(xtickVals)
    ax[i].set_yticks(ytickVals)
    
    # Set tick labels of each plot
    ax[i].set_xticklabels(xtickVals, rotation='vertical')
    ax[i].set_yticklabels(ytickVals)
    
    # Set aspect ratio
    ax[i].set_aspect('equal')
    
ax[0].set_ylabel('y [cm]')

# Need inputs for colorbar:
    # "ScalarMappable": the thing to map colors to
    # axes argument: which axes (singular or plural) the colorbar belongs to
fig.colorbar(mesh, ax=ax, label='Normalized Free Surface Height', location='bottom')
    


