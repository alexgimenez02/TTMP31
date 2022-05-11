from Bass import Bass
from music import *


def test():
    bass = Bass("Bass test", 80)

    bassPitches1   = [REST, A2, REST, A2, E2, D2, REST, D2, A2, G2, REST, G2, D2, C2] 
    bassPitches2   = [REST, C2, G2, FS2, REST, FS2, C2, B1, REST, B1, FS2, E2] 
    bassPitches3   = [REST, E2, E2, B1, E2, REST]
    
    bassDurations1 = [WN, QN, EN, EN, HN, QN, EN, EN, HN, QN, EN, EN, HN, QN] 
    bassDurations2 = [EN, EN, HN, QN, EN, EN, HN, QN, EN,EN, HN, QN]
    bassDurations3 = [EN, EN, QN, QN, HN, HN]

    bass.addPhrase(bassPitches1, bassDurations1)  
    bass.addPhrase(bassPitches2, bassDurations2)
    bass.addPhrase(bassPitches3, bassDurations3)

    bass.play_theme()

test()