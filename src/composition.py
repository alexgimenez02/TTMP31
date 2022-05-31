from piano import Piano
from electricguitar import electricGuitar
from acousticGuitar import acousticGuitar
from music import *

if "__main__" in __name__:
   score  = Score("Composition", 120)
   
   piano = Piano("Piano", 120, [0, 1])   
   electGuitar = electricGuitar("Electric guitar", 120, 2)   
   acGuitar = acousticGuitar("Acoustic guitar", 120, 3)
   
   # electGuitar
   pitches =  [SILENT, G5, G5, E5, D5, D5, DS5, DF5, C5, SILENT, D5, D5, SILENT]
   duration = [QN, DHN, WN, QN, DHN, SN, SN, DQN, DHN, HN, HN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [G5, G5, E5, A5, E5, G5, SILENT, DS5, DF5, C5, SILENT, C5, B4, A4, SILENT]
   duration =  [DHN, QN, SN, SN, SN, DHN, EN, QN, QN, HN, EN, QN, QN, HN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [D4, DS4, E4, SILENT, A4, E4, G4, G4, SILENT, G4, A4, SILENT, D5, C5, SILENT]
   duration = [QN, QN, DHN, QN, QN, QN, HN, DQN, EN, QN, HN, QN, HN, HN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches =  [D4, DS4, E4, SILENT, C5, D5, E5, G5, G5, SILENT, C6, C6, C6, SILENT, A5, E6, SILENT]
   duration = [QN, QN, DHN, QN, SN, SN, QN, EN, DHN, QN, DHN, QN, DQN, EN, QN, DHN, HN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [DS6, D6, F6, C6, DS6, AS5, GS5, F5, A5, G5, SILENT]
   duration = [HN, QN, EN, EN, EN, EN, EN, EN, EN, EN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [AS5, GS5, A5, G5, A5, SILENT, GS5, F5, SILENT, [D6, AS5], [C6, GS5], [D6,A5], [C6, G5], SILENT]
   duration = [QN, EN, QN, EN, QN, EN, EN, DHN, EN, EN, EN, EN, EN, EN]
   electGuitar.addToPhase(pitches, duration)

   pitches = [SILENT, C6, GS6, G6, SILENT, G6, F6, G6, D6, F6, SILENT, DS6, D6, C6, DS6, AS5, AS5, GS5, AS5, C6, SILENT, SILENT]
   duration = [EN, QN, HN, DQN, EN, QN, EN, EN, EN, DQN, QN, QN, QN, EN, HN, HN, HN, HN, HN, HN, EN, DHN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [[G4, D4, F3], [G4, D4, F3], [G4, D4, F3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [B4, FS4, B3], [B4, FS4, B3], [B4, F4, B3], [B4, FS4, B3], [C5, G4, C4], [D5, A4, D4], SILENT]
   duration = [HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, QN, WN, WN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [[G4, D4, F3], [G4, D4, F3], [G4, D4, F3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [A4, E4, A3], [B4, FS4, B3], [B4, F4, B3], [B4, FS4, B3], [B4, F4, B3], [C5, G4, C4], [C5, G4, C4], [D5, A4, D4], [D5, A4, D4], SILENT]
   duration = [HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, QN, QN, DHN, QN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, A5, A5, G5, A5, A5, A5, A5, SILENT, A5, C6, D6, SILENT, D6, C6, E6, SILENT]
   duration = [DHN, QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, A5, A5, G5, A5, A5, G5, A5, G5, E5, D5, E5, DS5, A4, SILENT]
   duration = [QN, HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, HN, HN, HN, HN]
   electGuitar.addToPhase(pitches, duration)
   electGuitar.create_score();
   
   # acGuitar
   firstchord = [[A3,E4,A4,C5,E5]]*5
   durationfirstchord = [QN,QN,QN,EN,EN]
   dynamicsfirstchord = [MP] * 5
   secondchord = [[G3,B3,E4,G4]] * 5
   durationsecondchord = [QN,QN,QN,EN,EN]
   dynamicssecondchord = [MP] * 5
   for i in range(32):
      acGuitar.addToPhase(firstchord,durationfirstchord,dynamicsfirstchord)
      acGuitar.addToPhase(secondchord,durationsecondchord,dynamicssecondchord)
   
   lastchord = [[AF3,EF4,AF4,CF5,EF5],REST]
   duration = [HN]*2
   dynamics = [MP]*2
   acGuitar.addToPhase(lastchord,duration,dynamics)
   acGuitar.create_score()
   
   
   # piano
   r_pitches = [[A3, C4, E4], [A3, C4, E4], [A3, C4, E4],     [B3, E4, G4], [B3, E4, G4], [B3, E4, G4]]
   r_durations = [DQN,            DQN,            QN,              DQN,          DQN,           QN] 
   l_pitches = [[A1, A2],        [A1, A2],     [A1, A2],         [E2, E3],    [E2, E3],      [E2, E3]]
   l_durations = [DQN,             DQN,           QN,                DQN,        DQN,           QN]    
   piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations, 2)    
   piano.create_score();   

   score.addPart(piano.l_hand_part)
   score.addPart(piano.r_hand_part)   
   score.addPart(electGuitar.part)
   score.addPart(acGuitar.part)
   
   Play.midi(score)   