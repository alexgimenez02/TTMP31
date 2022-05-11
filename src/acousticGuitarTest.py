from acousticGuitar import acousticGuitar
from music import *

if "__main__" in __name__:
   

   instr = acousticGuitar("Guitar test", 150)
    
   pitches1   = [E5, DS5, E5, DS5, E5, B4, D5, C5]
   durations1 = [SN, SN,  SN, SN,  SN, SN, SN, SN]
   pitches2   = [A4, REST, C4, E4, A4, B4, REST, E4]
   durations2 = [EN, SN,   SN, SN, SN, EN, SN,   SN]
   pitches3   = [GS4, B4, C5, REST, E4]
   durations3 = [SN,  SN, EN, SN,   SN]
   pitches4   = [C5, B4, A4]
   durations4 = [SN, SN, EN]
   
   instr.addToPhase(pitches1,duration1)
   instr.addToPhase(pitches2,duration2)
   instr.addToPhase(pitches3,duration3)
   instr.addToPhase(pitches4,duration4)
   

   instr.playTheme()
   
   