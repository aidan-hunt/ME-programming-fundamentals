# -*- coding: utf-8 -*-
"""
Aidan Hunt
ME 498K

Lecture 17 - Live
"""

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

plt.rcParams['figure.dpi'] = 199 # For Aidan's computer

#%% Ways we can specify colors

x = np.linspace(-1, 1, 100)
y = x**2

uwPurple = '#4b2e83'
uwGold = '#b7a57a'

fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0, 0].plot(x, y, color='b')
ax[0, 1].plot(x, y, color ='k')
ax[1, 0].plot(x, y, color=uwPurple)
ax[1, 1].plot(x, y, color =uwGold)

#%% Examples of working with color specs

# Get all the colors that are mapped to strings
allColors = dict(colors.get_named_colors_mapping())

# Convert hex to rgb
print('UW Purple:', colors.to_rgb(uwPurple))
print('UW Gold:', colors.to_rgb(uwGold))

#%% Colormaps

# A colormap "maps" a range of values to a range of colors

# Accessing built-in colormaps via mpl.colormaps
# Use dict-like notation with mpl.colormaps

import matplotlib as mpl

colormaps = mpl.colormaps
print(colormaps)
exMap = mpl.colormaps['viridis']

# Alternative approach: access via matplotlib.cm and cm.get_cmap
import matplotlib.cm as cm

exMap2 = cm.get_cmap('viridis')

# Get a list of colors corresponding to a listed colormap
colorList = exMap.colors

# A coarser version of the same colormap
coarseMap = cm.get_cmap('viridis', 8)

# Get color corresponding to a particular value
firstColor = coarseMap(0) # First color
lastColor = coarseMap(7) # Last color
anotherColor = coarseMap(6.6)

#%% Create our own colormaps

# Listed colormap example
uwMap_listed = colors.ListedColormap([uwPurple, 'white', uwGold], name='goDawgs')

# Linear segmented colormap example
uwMap_segmented = colors.LinearSegmentedColormap.from_list('goDawgs', [uwPurple, 'white', uwGold])










