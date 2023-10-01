# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:53:25 2023

@author: Aidan Hunt
"""

# Example of setter and getter methods for the color attribute (see last methods)

class MusicPlayer:
            
    # Define a constructor
    def __init__(self, color, songList=[]):
        '''
        Constructs and returns a MusicPlayer object with the given and,
        if provided, the given song list. The MusicPlayer's power is
        initialized to False and the MusicPlayer's volume is initialized
        to 0.
        '''
        self.power = False   # Power is well represented as a boolean
        self.volume = 0      # Volume is well represented as a numeric value
        self.color = color # Color is well represented as a string
        self.songList = songList   # Song list is well represented as a list of strings!
    
    # Define a function for turning the MusicPlayer on and off
    def togglePower(self):
        '''
        Toggles the MusicPlayer power. If the MusicPlayer is off, turns
        it on. If on, turns it off. A message is printed displaying the
        new power state.
        '''
        # Invert power
        self.power = not self.power
        
        # Print message
        if self.power:
            print('Powering music player on.')
        else:
            print('Powering music player off.')
    
    def changeVolume(self, newVolume):
        '''
        Given a new volume value between 0 and 100,
        sets the volume to be that value. If the volume
        value is invalid, the volume is not change and a
        message is printed.
        '''
        if 0 <= newVolume <= 100:
            self.volume = newVolume
        else:
            print('Invalid volume provided.')
            
    def addSong(self, song):
        '''
        Given a song name (as a string), adds the song
        to the song list if it a string. Otherwise, a
        message is printed saying the song cannot be added.
        '''
        if isinstance(song, str):
            self.songList.append(song)
        else:
            print(song, 'cannot be added to the queue.')
            
    def playSong(self, songNumber):
        '''
        Given the index of a song in the songList, removes
        the song from the list and "plays" it, and returns
        the song name as a string. If the songNumber
        provided is not a valid index, prints a message stating
        so.
        '''
        if 0 <= songNumber < len(self.songList):
            currSong = self.songList.pop(songNumber)
            print('Now playing:', currSong)
            return currSong
        else:
            print('Cannot play song.')
            return None  
        
    def __str__(self):
        '''
        Returns the songList of the MusicPlayer
        as its string representation.
        '''
        return str(self.songList)
    
    def __int__(self):
        '''
        Returns the length of the songList of the MusicPlayer
        as its int representation.
        '''
        return len(self.songList)
    
    def __float__(self):
        '''
        Returns the length of the songList of the MusicPlayer
        as its float representation.
        '''
        return float(self.__int__())
    
    @property
    def color(self):
        '''
        This function defines what is returned to the user when they use
        dot notation to get the color attribute of a MusicPlayer. Here,
        we are just returning value of the color attribute directly.
        '''
        return self.color
        
    @color.setter
    def color(self, newColor):
        '''
        This function defines what is returned to the user when they use
        dot notation to try to set the color attribute of a MusicPlayer.
        If the newColor provided is a string, we set the color attribute to 
        be newColor. Otherwise, we raise a TypeError.
        '''
        if type(newColor) == str:
            self.color = newColor
        else:
            raise TypeError('Provided color must be of type str.')
    