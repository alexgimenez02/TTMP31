from acousticGuitar import acousticGuitar
from music import *
import time

if "__main__" in __name__:
   

   instr = acousticGuitar("Guitar test", 60)
   
'''
fur elise example with STEEL_GUITAR
   #Notes 
   pitches1   = [E5, DS5, E5, DS5, E5, B4, D5, C5]
   durations1 = [SN, SN,  SN, SN,  SN, SN, SN, SN]
   pitches2   = [A4, REST, C4, E4, A4, B4, REST, E4]
   durations2 = [EN, SN,   SN, SN, SN, EN, SN,   SN]
   pitches3   = [GS4, B4, C5, REST, E4]
   durations3 = [SN,  SN, EN, SN,   SN]
   pitches4   = [C5, B4, A4]
   durations4 = [SN, SN, EN]
   
   #Adding the notes into the phase
   instr.addToPhase(pitches1,durations1)
   instr.addToPhase(pitches2,durations2)
   instr.addToPhase(pitches3,durations3)
   instr.addToPhase(pitches4,durations4)
   
   #Play the theme
   instr.playTheme()
'''   
    instr.playNote(Note(C4, QN))
   

   
   