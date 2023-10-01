# -*- coding: utf-8 -*-
"""
Aidan Hunt
5/15/2023

Lecture 15 - Live
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.dpi'] = 199

# Generate data
x = np.linspace(0, 2*np.pi, 25)
y = np.sin(x)

#%% Create a plot the "usual" way

# Create the figure
plt.figure()

# Plot the data
plt.plot(x, y)

# Add some labels
plt.xlabel('x')
plt.ylabel('y')
plt.title('A simple plot')

# Turn on the grid
plt.grid()

#%% Generate the same figure, another way

# Create a figure object and an associate axes object
fig, ax = plt.subplots()

# Talk to the axes object to plot
ax.plot(x, y)

# Add some labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('A simple plot')

# Turn on the grid
ax.grid(visible=True)

#%% Generate a slightly more complicated figure

# Create a figure with multiple axes
nRows = 2
nCols = 2
fig, ax = plt.subplots(nrows=nRows, ncols=nCols, layout='constrained', sharex=True, sharey=True)

# Talk to the axes object to plot
# Line specification as a 3 element string
    # a color
    # a line style
    # a marker type
line = ax[0, 0].plot(x[:6], y[:6], '-ro', alpha=0.25, label='Line1')
ax[0, 1].plot(x, y, ':k', label='Another line')
ax[1, 0].plot(x, y, '--gv', label='Yet another line')
ax[1, 1].plot(x[10:], y[10:], '-bs', label='No label')

# fig.set_facecolor('gray')
fig.set(facecolor='white', figwidth=8)

for i in range(nRows):
    for j in range(nCols):
        ax[i,j].set(xlabel='x', ylabel='y', title='A simple plot')
        ax[i,j].legend(handles=line)


