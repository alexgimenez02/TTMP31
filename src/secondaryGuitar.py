from music import *

class secondaryGuitar:
    name = ""
    bpm = 0
    score = None
    part = Part(24)  #GUITAR, NYLHON_GUITAR
   
    def __init__(self, name='Second Guitar', bpm=60):
        self.name = name
        self.score = Score(name,bpm)
   
    def playNote(self,note):
        '''
        plays a single note Play.midi(note)
        '''
        phrase = Phrase()
        phrase.addNote(note)
        Play.midi(part.addPhrase(phrase))
        

    def addToPhase(self,pitches,duration): 
        '''
        adds the notes (pitches) and the duration of them in the theme
        '''
        phrase = Phrase()
        phrase.addNoteList(pitches,duration)
        self.part.addPhrase(phrase)

    def changeTempo(self,tempo):
        '''
        changes the tempo of the theme
        '''
        pass
    
    def create_score(self):
        if self.part.getSize() > 0:
            self.score.addPart(self.part)

    def write_mdi(self,path):
        Write.midi(self.score,path)
        
    def playTheme(self):
        '''
        plays the theme Play.midi(theme)
        '''
        self.create_score()
        Play.midi(self.score)