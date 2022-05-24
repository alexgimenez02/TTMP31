from piano import Piano
from electricguitar import electricGuitar
from music import *

if "__main__" in __name__:
   score  = Score("Composition", 120)
   piano = Piano("Piano test", 120, [0, 1])
   electGuitar = electricGuitar("Electric guitar", 120, 2)   
      
   pitches = [SILENT, A5,     G5,      E5, D5,     D5, DS5, D5, C5]
   duration = [QN,    DHN,    WN,      QN, DHN,    SN, SN, DQN, DHN ]   
   electGuitar.addToPhase(pitches, duration)
   electGuitar.create_score();
   
   r_pitches = [[A3, C4, E4], [A3, C4, E4], [A3, C4, E4],     [B3, E4, G4], [B3, E4, G4], [B3, E4, G4]]
   r_durations = [DQN,            DQN,            QN,              DQN,          DQN,           QN] 
   l_pitches = [[A1, A2],        [A1, A2],     [A1, A2],         [E2, E3],    [E2, E3],      [E2, E3]]
   l_durations = [DQN,             DQN,           QN,                DQN,        DQN,           QN]    
   piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations, 2)    
   piano.create_score();   

   score.addPart(piano.l_hand_part)
   score.addPart(piano.r_hand_part)   
   score.addPart(electGuitar.part)   
   
   Play.midi(score)   