from Bass import Bass
from music import *


if "__main__" in __name__:
   
    bass = Bass("Bass test", 120)

    #Loop
    bassPitch   = [SILENT, SILENT, A2, A2, A2, G2, G2, G2, F2, F2, F2, E2, E2, E2, A2, A2, A2, G2, G2, G2, F2, F2, F2, B2, A2, C3, C3, C3, E3, D3, C3, C3, C3, G3, C3, A2, A2, A2, C3, C3, E3, G3, A2, A2, F3, D3, C3, G3, C3, G2,G2,G2,F2,F2,F2,E2,E2,E2,A2,A2,A2,G2,G2,G2,F2,F2,F2,B2,A2,C3,C3,C3, E3, D3, C3, C3, C3, G3, C3, A2, A2, A2, C3, C3,E3,G3,A3,A3,F3,D3,C3,G3,C3,C3] 
    
    bassDuration = [WN, WN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, EN, EN, QN, EN ,EN, EN, EN, QN, EN ,EN, QN, QN, QN, QN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN ,EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, QN, QN, QN, QN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN] 
 
    bass.addToPhase(bassPitch, bassDuration)  

    bass.playTheme()
