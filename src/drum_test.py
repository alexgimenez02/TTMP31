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
   
   #Change Tempo and add Snare
   drum.changeTempo(50.0)
   snarePitches   = [REST, SNR] * 4
   snareDurations = [QN,   QN] * 4
   drum.addToPhrase(snarePitches, snareDurations)
   drum.playTheme()
   
   time.sleep(10.0)
   
   #Change tempo again and add the Hi Hat
   drum.changeTempo(125.0)
   hiHatPitches   = [CHH] * 15 + [OHH]
   hiHatDurations = [EN] * 15  + [EN]
   drum.addToPhrase(hiHatPitches, hiHatDurations)
   drum.playTheme()
   
   time.sleep(7.0)
   
   #Loop what we have in order to produce the base.
   Mod.repeat(drum.score, 8)
   drum.playTheme()
   

   
test()