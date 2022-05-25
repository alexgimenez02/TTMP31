from music import *

class acousticGuitar:
    name = ""
    bpm = 0
    score = None
    instrument = STEEL_GUITAR
    part = None
   
    def __init__(self, name='Acoustic Guitar', bpm=60, part_num=0):
        self.name = name
        self.score = Score(name,bpm)
        self.part = Part(self.instrument, part_num)  # Steel Guitar
   
    def playNote(self,note):
        '''
        plays a single note Play.midi(note)
        '''
        phrase = Phrase()
        phrase.addNote(note)
        prt = Part(self.instrument)
        prt.addPhrase(phrase)
        Play.midi(prt)
        

    def addToPhase(self,pitches,duration, dynamics): 
        '''
        adds the notes (pitches) and the duration of them in the theme
        '''
        phrase = Phrase()
        phrase.addNoteList(pitches,duration,dynamics=dynamics)
        self.part.addPhrase(phrase)
        

    def changeTempo(self,tempo):
        '''
        changes the tempo of the theme
        '''
        self.score.setTempo(tempo)
    
    def create_score(self):
        if self.part.getSize() > 0:
            self.score.addPart(self.part)

    def write_mdi(self,path):
        self.create_score()
        Write.midi(self.score,path)
        
    def playTheme(self):
        '''
        plays the theme Play.midi(theme)
        '''
        self.create_score()
        Play.midi(self.score)