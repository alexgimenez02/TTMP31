from drum import Drums
from music import *
import time

def test():
   drum = Drums("Drums Test", 125.0)
   
   #Basic Bass test
   bassPitches   = [BDR, REST] * 4
   bassDurations = [QN,  QN] * 4
   drum.addToPhrase(bassPitches, bassDurations)
   drum.playTheme()
   
   #To avoid mixing sounds
   time.sleep(4.0)
   
   #Play Note test
   n = Note(PEDAL_HI_HAT, QN)
   drum.playNote(n)

   time.sleep(1.0)
   
   #Change Tempo test and add Snare
   drum.changeTempo(50.0)
   snarePitches   = [REST, SNR] * 4
   snareDurations = [QN,   QN] * 4
   drum.addToPhrase(snarePitches, snareDurations)
   drum.playTheme()
   
test()