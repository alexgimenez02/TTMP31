from music import *

class Drums:
   bpm = 0
   score = None
   part = None
   
   def __init__(self, name='Drums', bpm=125.0, part_num = 0):
      self.name = name
      self.bpm = bpm
      self.score = Score(name, bpm)
      self.part = Part("Drums", part_num, 9)  # ELECTRIC GUITAR
      
   def playNote(self,note):
      testPart = Part("Drums", 0, 9)
      testPhrase = Phrase()
      testPhrase.addNote(note)
      testPart.addPhrase(testPhrase)      
      Play.midi(testPart)
      testPhrase.empty()
      testPart.empty()
    
   def addPhrase(self,pitches,duration,startTime=None):
      phrase = Phrase(startTime)
      phrase.addNoteList(pitches, duration)
      self.part.addPhrase(phrase)
    
   def changeTempo(self,tempo):

      self.score = Score(self.name, tempo)
    
   def create_score(self):
      if self.part.getSize() > 0:
         self.score.addPart(self.part)

   def play_theme(self):
      self.create_score()
      Play.midi(self.score)
      
   def write_mdi(self, path):
      Write.midi(self.score, path)    