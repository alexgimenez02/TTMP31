from secondaryGuitar import secondaryGuitar
from music import *

if "__main__" in __name__:
   

   instr = secondaryGuitar("Guitar test", 150)
    
   pitches = [E5, D5, E5, D5, E5, B4]
   duration = [QN, QN, QN, QN, QN, QN]
   
   instr.addToPhase(pitches,duration)
   

   instr.playTheme()
   
   