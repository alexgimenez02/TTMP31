import abc
from abc import ABC, abstractmethod

class Instrument(ABC):
    '''
    Abstract class to implement various instruments.
    Atributes: theme (series of notes to be player)
    Classes: __init__ (constructor) -> Initilizes the theme theme = Phrase()
             playNote(self,notes)   -> plays a single note  
             addToPhase(self,pitches,duration) -> adds diferent notes with diferents durations (see examples from jython)
             changeTempo(self,tempo) -> self explanatory, changes the tempo of the theme
             playTheme(self) -> plays the theme of the instrument
             Examples:
                playNote.py
                furElise.py
                axelF.py
    '''
    @property
    @abstractmethod
    def theme(self):
        '''
        Atribute, do not implement as a function
        '''
        pass
    @abstractmethod
    def __init__(self):
        '''
        initialize the theme atribute, and add the type of instrument with theme.setInstrument("Instrument_name")
        '''
        pass
    @abstractmethod
    def playNote(self,note):
        '''
        plays a single note Play.midi(note)
        '''
        pass
    @abstractmethod
    def addToPhase(self,pitches,duration): 
        '''
        adds the notes (pitches) and the duration of them in the theme
        '''
        pass
    @abstractmethod
    def changeTempo(self,tempo):
        '''
        changes the tempo of the theme
        '''
        pass
    @abstractmethod
    def playTheme(self):
        '''
        plays the theme Play.midi(theme)
        '''
        pass
    
    
