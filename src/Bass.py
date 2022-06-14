from music import *

class Bass:
    name = ""
    bpm = 0
    score = None
    part = None
   
    def __init__(self, name = 'Bass', bpm = 60, part_num = 0):
        self.name = name
        self.bpm = bpm
        self.score = Score(name, bpm)
        self.part = Part(ACOUSTIC_BASS, part_num) #BASS
   
    def playNote(self, note):
        '''
        plays a single note Play.midi(note)
        '''
        phrase = Phrase()
        phrase.addNote(note)
        part.addPhrase(phrase)
        Play.midi(part)
        

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
        self.score = Score(self.name, tempo)
    
    def create_score(self):
        if self.part.getSize() > 0:
            self.score.addPart(self.part)
        
    def playTheme(self):
        '''
        plays the theme Play.midi(theme)
        '''
        self.create_score()
        Play.midi(self.score)

    def write_mdi(self, path):
        Write.midi(self.score, path)