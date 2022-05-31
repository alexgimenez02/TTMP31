from drum import Drums
from music import *
import time

def test():
   drum = Drums("Drums Test", 60.0)
   
   #Intro
   hiHatPitches   = [CHH, CHH]
   hiHatDurations = [QN, QN]
   
   highTomPitches = [REST, 40, 40, 50, 50, 47, 47, 41]
   highTomDurations = [SN, SN, SN, SN, SN, SN, SN, SN]
   
   introPitches = hiHatPitches + highTomPitches
   introDurations = hiHatDurations + highTomDurations
   
   drum.addPhrase(introPitches, introDurations)
   
   #Base
   crashPitches = [CC1]
   crashDurations = [QN]
   drum.addPhrase(crashPitches, crashDurations)

   
   bassPitches   = [BDR, REST, BDR, REST, BDR, REST, BDR] * 60
   bassDurations = [QN, EN, EN, EN, EN, EN, EN] * 60
   drum.addPhrase(bassPitches, bassDurations, 4.0)
   
   snarePitches   = [REST, SNR] * 2 * 60
   snareDurations = [QN, QN]*2 * 60
   drum.addPhrase(snarePitches, snareDurations, 4.0)
   
   hiHatPitches   = [CHH] *8 * 60
   hiHatDurations = [EN] * 8 * 60
   drum.addPhrase(hiHatPitches, hiHatDurations, 4.0)
   
   drum.play_theme()
   
   """
   #drum.playTheme()
   print("Scores: ",drum.score.getSize())
   print("Parts: ",drum.part.getSize())
   print(drum.part)
   """
test()
