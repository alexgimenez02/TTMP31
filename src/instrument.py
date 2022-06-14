import abc
from abc import ABC, abstractmethod


class Instrument(ABC):
    '''
    Abstract class to implement various instruments.
    Atributes: theme (series of notes to be player)
    Classes: __init__ (constructor) -> Initilizes the theme theme
             playNote(self,notes)   -> plays a single note  
             addToPhase(self,pitches,duration) -> adds diferent notes with diferents durations (see examples from jython)
             changeTempo(self,tempo) -> self explanatory, changes the tempo of the theme
             playTheme(self) -> plays the theme of the instrument
             Examples:
                playNote.py
                furElise.py
                axelF.py
    '''
    name = ""
    bpm = 0
    score = None
    part = None  # SET part = Part(instrument, channel) Piano Example: part = Part(PIANO, 0)

    @abstractmethod
    def __init__(self, name, bpm=60):
        '''
        initialize the theme atribute, and add the type of instrument with theme.setInstrument("Instrument_name")
        '''
        self.name = name
        self.score = Score(name, bpm)

    @abstractmethod
    def playNote(self, note):
        '''
        plays a single note Play.midi(note)
        '''
        pass

    @abstractmethod
    def addPhrase(self, pitches, duration):
        phrase = Phrase()
        phrase.addNoteList(pitches, duration)
        self.part.addPhrase(phrase)

    @abstractmethod
    def changeTempo(self, tempo):
        '''
        changes the tempo of the theme
        '''
        pass

    @abstractmethod
    def create_score(self):
        if self.part.getSize() == 0: return
        self.score.addPart(self.part)

    @abstractmethod
    def write_mdi(self, path):
        Write.midi(self.score, path)

    @abstractmethod
    def play_theme(self):
        self.create_score()
        Play.midi(self.score)
