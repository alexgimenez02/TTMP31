from secondaryGuitar import secondaryGuitar
from music import *

if "__main__" in __name__:
   

   instr = secondaryGuitar("Guitar test", 200)
    
   pitches = [C4, E4, F2, [B2, C2, D4]]
   duration = [QN, QN, QN, WN]
   
   instr.addToPhase(pitches,duration)
   

   instr.playTheme()
   
   