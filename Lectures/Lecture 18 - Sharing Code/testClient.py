# -*- coding: utf-8 -*-
"""
Aidan Hunt

Client script

"""

# Show how to import a simple test module

# Trying to import testModule (which is in a subfolder) doesn't work
import testModule1

#%% Add the directory that the module lives in to the system path
    # Stays in system path until you restart your IDE
import sys
import os

modulePath = os.path.join('.', 'Test Modules')
sys.path.append(modulePath)

# Now try importing
import testModule2
    # Any code statements are run when importing
    # But not-rerun on repeat imports?
    
# Use functions from the module

testModule2.printMessage()

num = testModule2.addNumbers(5, 3)

#%% Creating/importing packages/submodules

import testPackage

# testPackage.module1 # Not imported by default

#%% from testPackage import module1, module2, module3

