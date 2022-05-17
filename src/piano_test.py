from piano import Piano
from music import *


def test():
    piano = Piano("Piano test", 70)

    r_pitches = [[A3, C4, E4], [A3, C4, E4], [A3, C4, E4],     [B3, E4, G4], [B3, E4, G4], [B3, E4, G4]]
    r_durations = [DQN,            DQN,            QN,              DQN,          DQN,           QN]
 
    l_pitches = [[A1, A2],        [A1, A2],     [A1, A2],         [E2, E3],    [E2, E3],      [E2, E3]]
    l_durations = [DQN,             DQN,           QN,                DQN,        DQN,           QN]    

    piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations, 10)    

    piano.play_theme()

test()
