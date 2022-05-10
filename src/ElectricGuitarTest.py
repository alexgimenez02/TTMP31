from electricguitar import electricGuitar
from music import *

if "__main__" in __name__:
   

   instr = secondaryGuitar("Guitar test", 150)
    
   pitches = [G5, G5, E5, D5, SILENT, D5, DS5, D5, C5, D5]
   duration = [HN, QN, QN, DHN, QN, EN, EN, EN, HN, HN]
   
   instr.addToPhase(pitches, duration)
   

   instr.playTheme()