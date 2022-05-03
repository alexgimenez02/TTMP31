from piano import Piano
from music import *


def test():
    piano = Piano("Piano test", 80)

    l_pitches = [C4, E4, G4, C4]
    l_durations = [QN, QN, QN, QN]

    r_pitches = [[C3, E5, G5]]
    r_durations = [WN]

    piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations)

    pitches = [D4, E4, C4]
    durations = [QN, QN, QN]
    piano.addPhrase(pitches, durations)


    piano.play_theme()

test()
