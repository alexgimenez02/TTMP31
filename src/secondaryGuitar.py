

class secondaryGuitar:
   theme
   
   def __init__(self):
      self.theme = Part(ACOUSTIC_GUITAR,0)
      
   
    def playNote(self,note):
        '''
        plays a single note Play.midi(note)
        '''
        pass
    
    def addToPhase(self,pitches,duration): 
        '''
        adds the notes (pitches) and the duration of them in the theme
        '''
        pass
    
    def changeTempo(self,tempo):
        '''
        changes the tempo of the theme
        '''
        pass
    
    def playTheme(self):
        '''
        plays the theme Play.midi(theme)
        '''
        pass