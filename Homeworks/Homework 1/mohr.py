"""
[Your name goes here]

[Your program summary goes here]
"""

# Imports
import numpy as np

# Stress state 1
sigmaX1 = 50
sigmaY1 = 10
tauXY1 = -15
sigmaAve1 = (sigmaX1 + sigmaY1) / 2
maxShear1 = np.sqrt(((sigmaX1-sigmaY1)/2)**2 + tauXY1**2)
sigmaMax1 = sigmaAve1 + maxShear1
sigmaMin1 = sigmaAve1 - maxShear1
arg1 = 2*tauXY1 / (sigmaX1 - sigmaY1)
thetaP1 = np.arctan(arg1) / 2
thetaP1 = thetaP1 * 180 / np.pi
print('Stress state:')
print('Maximum principal stress:', round(sigmaMax1, 2), 'MPa')
print('Minimum principal stress:', round(sigmaMin1, 2), 'MPa')
print('Maximum shear stress:', round(maxShear1, 2), 'MPa')
print('Angle of principal stresses', round(thetaP1, 2), 'Degrees')
print()

# Stress state 2
sigmaX2 = -50
sigmaY2 = 10
tauXY2 = -15
sigmaAve2 = (sigmaX2 + sigmaY2) / 2
maxShear2 = np.sqrt(((sigmaX2-sigmaY2)/2)**2 + tauXY2**2)
sigmaMax2 = sigmaAve2 + maxShear2
sigmaMin2 = sigmaAve2 - maxShear2
arg2 = 2*tauXY2 / (sigmaX2 - sigmaY2)
thetaP2 = np.arctan(arg2) / 2
thetaP2 = thetaP2 * 180 / np.pi
print('Stress state:')
print('Maximum principal stress:', round(sigmaMax2, 2), 'MPa')
print('Minimum principal stress:', round(sigmaMin2, 2), 'MPa')
print('Maximum shear stress:', round(maxShear2, 2), 'MPa')
print('Angle of principal stresses', round(thetaP2, 2), 'Degrees')
print()

# Stress state 3
sigmaX3 = 30
sigmaY3 = -30
tauXY3 = 30
sigmaAve3 = (sigmaX3 + sigmaY3) / 2
maxShear3 = np.sqrt(((sigmaX3-sigmaY3)/2)**2 + tauXY3**2)
sigmaMax3 = sigmaAve3 + maxShear3
sigmaMin3 = sigmaAve3 - maxShear3
arg3 = 2*tauXY3 / (sigmaX3 - sigmaY3)
thetaP3 = np.arctan(arg3) / 2
thetaP3 = thetaP3 * 180 / np.pi
print('Stress state:')
print('Maximum principal stress:', round(sigmaMax3, 2), 'MPa')
print('Minimum principal stress:', round(sigmaMin3, 2), 'MPa')
print('Maximum shear stress:', round(maxShear3, 2), 'MPa')
print('Angle of principal stresses', round(thetaP3, 2), 'Degrees')
print()