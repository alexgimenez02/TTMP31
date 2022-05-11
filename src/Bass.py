from music import *

class Bass:
    name = ""
    bpm = 0
    score = None
    part = Part(BASS)
   
    def __init__(self, name = 'Bass', bpm = 60):
        self.name = name
        self.score = Score(name, bpm)
   
    def playNote(self, note):
        '''
        plays a single note Play.midi(note)
        '''
        notePart = Part(BASS)
        phrase = Phrase()
        phrase.addNote(note)
        notePart.addPhrase(phrase)
        Play.midi(notePart)
        

    def addToPhase(self, pitches, duration): 
        '''
        adds the notes (pitches) and the duration of them in the theme
        '''
        phrase = Phrase()
        phrase.addNoteList(pitches, duration)
        self.part.addPhrase(phrase)

    def changeTempo(self, tempo):
        '''
        changes the tempo of the theme
        '''
        pass
    
    def create_score(self):
        self.score.addPart(self.part)
        
    def playTheme(self):
        '''
        plays the theme Play.midi(theme)
        '''
        self.create_score()
        Play.midi(self.score)

    def write_mdi(self, path):
        Write.midi(self.score, path)