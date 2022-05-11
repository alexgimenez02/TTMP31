from piano import Piano
from music import *


def test():
    piano = Piano("Piano test", 80)

    l_pitches = [[C3, E3, G3]]
    l_durations = [WN]
 
    r_pitches = [C4, E4, G4, C4]
    r_durations = [QN, QN, QN, QN]    

    piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations)
   

    l_pitches = [REST]
    l_durations = [WN]
    
    r_pitches = [D4, E4, C4, REST]
    r_durations = [QN, QN, QN, QN]
    piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations)
        
    
    r_pitches = [F4, A4, C5, C5]
    r_durations = [QN, QN, QN, QN]

    l_pitches = [[F3, A3, C4]]
    l_durations = [WN]

    piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations)
    
    r_pitches = [F4]
    r_durations = [WN]

    l_pitches = [REST]
    l_durations = [WN]

    piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations)


    piano.play_theme()

test()
