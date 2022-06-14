from acousticGuitar import acousticGuitar
from music import *
import time

'''
TODO:

Search how to add a natural sign to each note on the composition
Loop both chords into the fully extend of the composition
Add the final tempo (?)

'''


if "__main__" in __name__:
   
   
   instr = acousticGuitar("Guitar test", 120)
   
   #Notes
   
   firstchord = [[AF3,EF4,AF4,CF5,EF5]]*5
   durationfirstchord = [QN,QN,QN,EN,EN]
   dynamicsfirstchord = [MP] * 5
   secondchord = [[GF3,BF3,EF4,GF4]] * 5
   durationsecondchord = [QN,QN,QN,EN,EN]
   dynamicssecondchord = [MP] * 5
   for i in range(32):
      instr.addToPhase(firstchord,durationfirstchord,dynamicsfirstchord)
      instr.addToPhase(secondchord,durationsecondchord,dynamicssecondchord)
   
   lastchord = [[AF3,EF4,AF4,CF5,EF5],REST]
   duration = [HN]*2
   dynamics = [MP]*2
   instr.addToPhase(lastchord,duration,dynamics)
   
   instr.playTheme()
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
   # instr.playNote(Note(C4, QN))
   

   
   