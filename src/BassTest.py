from Bass import Bass
from music import *


def test():
    bass = Bass("Bass test", 80)

    bassPitch   = [REST, AS0, REST, C1, EF1, C1, REST, AS0, D2, G2, REST, G2, D2, AS0] 
    
    bassDuration = [WN, QN, EN, EN, HN, QN, EN, EN, HN, QN, EN, EN, HN, QN] 

    bass.addToPhase(bassPitch, bassDuration)  

    bass.playTheme()

test()