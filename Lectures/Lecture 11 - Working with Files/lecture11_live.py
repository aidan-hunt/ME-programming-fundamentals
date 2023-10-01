# -*- coding: utf-8 -*-
"""
Aidan Hunt
5/1/2023

Lecture 11 - Working with Files

Scalability

Functions -> factor out redundancy and make our code flexible

def someFunction(inputParam1, inputParam2, optionalParam=defaultValue)

Files?
"""

#%% Motivation
def readFile(fileName):
    # Simple function that reads contents of text file and prints it out
    with open(fileName, 'r') as file:
        data = file.read()
        
    print(data)
    
fileName = 'example1.txt'

# readFile(fileName)

#%% Tools Python has for working with files

import os

# Current working directory
cwd = os.getcwd()

fileList = os.listdir()

#%% Reading text files - file paths

# readFile('example1.txt')

# Relative path - tells your computer how to access a file, starting from the cwd
filePath = '.\\Additional Files\\example3.txt'
readFile(filePath)

# Absolute path - tells your computer how to access a file, starting from the home directory
homeDir = os.path.expanduser('~')
absPath = cwd + '\\Additional Files\\example3.txt'

#%% How to construct paths programmatically

# Relative paths
fullPath = '.'
print(fullPath)
fullPath = os.path.join(fullPath, 'Additional Files')
print(fullPath)
fullPath = os.path.join(fullPath, 'example3.txt')
print(fullPath)

readFile(fullPath)

#%% Absolute paths - a little more to stick together

absPath = os.path.expanduser('~')
print(absPath)

subDirs = ['MREL Dropbox', 'Aidan Hunt', 'STEP-UP - ME 498', 'Lectures',
           'Lecture 11 - Working with Files', 'Additional Files']
for s in subDirs:
    absPath = os.path.join(absPath, s)
    print(absPath)
    
readFile(os.path.join(absPath, 'example3.txt'))

#%% Pattern matching for filenames
# Find all files in a particular directory that match a given naming convention

# Note: working with relative paths
import glob

# fileList = glob.glob('.\\Additional Files\\Even more files\\example*.txt')

fileList = glob.glob('.\\**\\example*.txt')

