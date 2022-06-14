from piano import Piano
from electricguitar import electricGuitar
from acousticGuitar import acousticGuitar
from Bass import Bass
from drum import Drums
from music import *
from gui import *
import time


score  = Score("Composition", 120)
auxScore = Score("CompositionToSave", 120)

piano = Piano("Piano test", 120, [0, 1])
electGuitar = electricGuitar("Electric guitar", 120, 2)   
acGuitar = acousticGuitar("Acoustic guitar", 120, 3)
drum = Drums("Drums", 120.0, 4)
bass = Bass("Bass", 120, 5)  

def composition():
      # SILENCE INTRO:
   pitches_intro =  [SILENT]
   duration_intro = [WN]
   # -------------------------------------------------
   # drum
     #Intro
   hiHatPitches   = [CHH, CHH]
   hiHatDurations = [HN, HN]
   
   highTomPitches = [REST, 40, 40, 50, 50, 47, 47, 41]
   highTomDurations = [EN, EN, EN, EN, EN, EN, EN, EN]
   
   introPitches = hiHatPitches + highTomPitches
   introDurations = hiHatDurations + highTomDurations
   
   drum.addPhrase(introPitches, introDurations)
   
      #Base
   crashPitches = [CC1]
   crashDurations = [HN]
   drum.addPhrase(crashPitches, crashDurations)
   
   
   bassPitches   = [BDR, REST, BDR, REST, BDR, REST, BDR] * 30
   bassDurations = [HN, QN, QN, QN, QN, QN, QN] * 30
   drum.addPhrase(bassPitches, bassDurations, 4.0)
   
   snarePitches   = [REST, SNR] * 2 * 30
   snareDurations = [HN, HN]*2 * 30
   drum.addPhrase(snarePitches, snareDurations, 4.0)
   
   hiHatPitches   = [CHH] *8 * 30
   hiHatDurations = [QN] * 8 * 30
   drum.addPhrase(hiHatPitches, hiHatDurations, 4.0)
   
   drum.create_score();
   # -------------------------------------------------
   #Bass
   
   bassPitchOffset = [SILENT, SILENT]
   bassDurationOffset = [WN,WN]  
   
   bassPitch   =  [A2, A2, A2, G2, G2, G2, F2, F2, F2, E2, E2, E2, A2, A2, A2, G2, G2, G2, F2, F2, F2, B2, A2, C3, C3, C3, E3, D3, C3, C3, C3, G3, C3, A2, A2, A2, C3, C3, E3, G3, A2, A2, F3, D3, C3, G3, C3, G2,G2,G2,F2,F2,F2,E2,E2,E2,A2,A2,A2,G2,G2,G2,F2,F2,F2,B2,A2,C3,C3,C3, E3, D3, C3, C3, C3, G3, C3, A2, A2, A2, C3, C3,E3,G3,A3,A3,F3,D3,C3,G3,C3,C3] 
   bassDuration =  [QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, EN, EN, QN, EN ,EN, EN, EN, QN, EN ,EN, QN, QN, QN, QN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN ,EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, QN, QN, QN, QN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN]
   
   bassPitchOutro = [G2,G2,G2,F2,F2,F2,E2,E2,E2,A2,A2,A2,G2,G2,G2,F2,F2,F2,B2,A2,C3,C3,C3, E3, D3, C3, C3, C3, G3, C3, A2, A2, A2, C3, C3,E3,G3,A3,A3,F3,D3,C3,G3,C3,C3]
   bassDurationOutro = [QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, QN, QN, QN, QN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN]
   
   bassPitches = bassPitchOffset + 3 * bassPitch + bassPitchOutro
   bassDurations = bassDurationOffset + 3 * bassDuration + bassDurationOutro
   
   bass.addToPhase(bassPitches, bassDurations)  
   
   bass.create_score();
   
   # electGuitar
   electGuitar.addToPhase(pitches_intro, duration_intro)
   pitches =  [SILENT, A5, G5, E5, D5, D5, DS5, D5, C5, SILENT, E5, D5, SILENT]
   duration = [QN, DHN, WN, QN, DHN, SN, SN, DQN, DHN, HN, HN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, G5, E5, A5, E5, G5, SILENT, DS5, D5, C5, SILENT, C5, B4, A4, SILENT]
   duration =  [DHN, QN, SN, SN, SN, DHN, DEN, QN, QN, HN, EN, QN, QN, HN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [D4, DS4, E4, SILENT, A4, E4, G4, G4, SILENT, G4, A4, SILENT, D5, C5, SILENT]
   duration = [QN, QN, DHN, HN, QN, QN, HN, DQN, EN, QN, HN, QN, HN, HN, HN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches =  [D4, DS4, E4, SILENT, C5, D5, E5, G5, G5, SILENT, D6, C6, C6, SILENT, A5, E6, SILENT]
   duration = [QN, QN, DHN, QN, SN, SN, QN, EN, DHN, QN, DHN, QN, DQN, EN, QN, DHN, HN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [B5, A5, A5, G5, A5, B5, A5, A5, SILENT, A5, C6, D6, SILENT, D6, C6, E6, SILENT]
   duration = [DHN, QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, B5, A5, G5, A5, B5, G5, A5, G5, E5, D5, E5, DS5, A4, SILENT]
   duration = [QN, HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, HN, HN, HN, DHN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches =  [G5, E5, D5, D5, DS5, D5, C5, SILENT, E5, D5, SILENT]
   duration = [WN, QN, DHN, SN, SN, DQN, DHN, HN, HN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, G5, E5, A5, E5, G5, SILENT, DS5, D5, C5, SILENT, C5, B4, A4, SILENT]
   duration =  [DHN, QN, SN, SN, SN, DHN, DEN, QN, QN, HN, EN, QN, QN, HN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [B5, A5, A5, G5, A5, B5, A5, A5, SILENT, A5, C6, D6, SILENT, D6, C6, E6, SILENT]
   duration = [DHN, QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, B5, A5, G5, A5, B5, G5, A5, G5, E5, D5, E5, DS5, A4, SILENT]
   duration = [QN, HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, HN, HN, HN, HN]
   electGuitar.addToPhase(pitches, duration)
   electGuitar.create_score();
   # -------------------------------------------------
   
   # acGuitar
   firstchord = [[A3, E4, A4, C5, E5]]*5
   durationfirstchord = [QN, QN, QN, EN, EN]
   dynamicsfirstchord = [MP] * 5
   secondchord = [[G3, B3, E4, G4]] * 5
   durationsecondchord = [QN, QN, QN, EN, EN]
   dynamicssecondchord = [MP] * 5   
   
   acGuitar.addToPhase(pitches_intro, duration_intro, [MP])
   
   for i in range(30):
      acGuitar.addToPhase(firstchord,durationfirstchord,dynamicsfirstchord)
      acGuitar.addToPhase(secondchord,durationsecondchord,dynamicssecondchord)
   
   lastchord = [[A3, E4, A4, C5, E5], REST]
   duration = [HN]*2
   dynamics = [MP]*2
   acGuitar.addToPhase(lastchord, duration, dynamics)
   acGuitar.create_score()
   # -------------------------------------------------
   
   # piano
   pitches_intro =  [SILENT]
   duration_intro = [WN]   
   piano.addPhraseTwoHands(pitches_intro, duration_intro, pitches_intro, duration_intro)    
   
   r_pitches1 = [[A3, C4, E4],     [A3, C4, E4],      [A3, C4, E4],            [B3, E4, G4],     [B3, E4, G4], A3,      C4, E4]
   r_durations1 = [DQN,            DQN,                   QN,                     DQN,                QN,     EN,       EN, EN] 
   
   r_pitches2 = [[A3, C4, E4],     [A3, C4, E4],        [A3, C4, E4],         [B3, E4, G4],      [B3, E4, G4],         A4,G4]
   r_durations2 = [DQN,            DQN,                    QN,                    DQN,               DQN,              EN, EN]
     
   r_pitches3 = [[A3, C4, E4, A4], [A3, C4, E4, A4],        D4,DS4,              [B3, E4, G4],        [B3, E4, G4],    DS4,D4]
   r_durations3 = [DQN,            DQN,                     EN, EN,                  DQN,                 DQN,          EN, EN]     
   
   r_pitches4 = [[A3, C4, E4],     [A3, C4, E4],        [A3, C4, E4],         [B3, E4, G4],      [B3, E4, G4],       [B3, E4, G4],]
   r_durations4 = [DQN,            DQN,                    QN,                    DQN,               DQN,                QN,]
   
   r_pitches = r_pitches1 + r_pitches2 + r_pitches3 + r_pitches4
   r_durations = r_durations1 + r_durations2 + r_durations3 + r_durations4
   
   
   l_pitches1 = [[A1, A2],                    [A1, A2],           [A1, A2],             [E2, E3],           [E2, E3],            [E2, E3]]
   l_durations1 = [DQN,                         DQN,                 QN,                  DQN,                DQN,                  QN]    
   
   l_pitches2 = [ SILENT, [A1, A2],        SILENT,[A1, A2],       [A1, A2],         SILENT,[E2, E3],    SILENT,[E2, E3],       [E2, E3]]
   l_durations2 = [EN, QN,                 EN, QN,                  QN,                 EN, QN,             EN, QN,               QN]   
      
   l_pitches = 2 * l_pitches1 + l_pitches2 + l_pitches1
   l_durations = 2 * l_durations1 + l_durations2 + l_durations1
   
   piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations, 7)    
   piano.create_score(); 
      
def saveScore():
    
   
   composition()
   
   if pianoCheck.isChecked():
      auxScore.addPart(piano.l_hand_part)
      auxScore.addPart(piano.r_hand_part)   
   if cGuitarCheck.isChecked():
      auxScore.addPart(electGuitar.part)   
   if mGuitarCheck.isChecked():
      auxScore.addPart(acGuitar.part)
   if drumsCheck.isChecked():
      auxScore.addPart(drum.part)
   if bassCheck.isChecked():
      auxScore.addPart(bass.part)

def mainSong():
   
   #MAIN COMPOSITION
   print "Playing..."
       # SILENCE INTRO:
   pitches_intro =  [SILENT]
   duration_intro = [WN]
   # -------------------------------------------------
   # drum
     #Intro
   hiHatPitches   = [CHH, CHH]
   hiHatDurations = [HN, HN]
   
   highTomPitches = [REST, 40, 40, 50, 50, 47, 47, 41]
   highTomDurations = [EN, EN, EN, EN, EN, EN, EN, EN]
   
   introPitches = hiHatPitches + highTomPitches
   introDurations = hiHatDurations + highTomDurations
   
   drum.addPhrase(introPitches, introDurations)
   
      #Base
   crashPitches = [CC1]
   crashDurations = [HN]
   drum.addPhrase(crashPitches, crashDurations)
   
   
   bassPitches   = [BDR, REST, BDR, REST, BDR, REST, BDR] * 30
   bassDurations = [HN, QN, QN, QN, QN, QN, QN] * 30
   drum.addPhrase(bassPitches, bassDurations, 4.0)
   
   snarePitches   = [REST, SNR] * 2 * 30
   snareDurations = [HN, HN]*2 * 30
   drum.addPhrase(snarePitches, snareDurations, 4.0)
   
   hiHatPitches   = [CHH] *8 * 30
   hiHatDurations = [QN] * 8 * 30
   drum.addPhrase(hiHatPitches, hiHatDurations, 4.0)
   
   drum.create_score();
   # -------------------------------------------------
   #Bass
   
   bassPitchOffset = [SILENT, SILENT]
   bassDurationOffset = [WN,WN]  
   
   bassPitch   =  [A2, A2, A2, G2, G2, G2, F2, F2, F2, E2, E2, E2, A2, A2, A2, G2, G2, G2, F2, F2, F2, B2, A2, C3, C3, C3, E3, D3, C3, C3, C3, G3, C3, A2, A2, A2, C3, C3, E3, G3, A2, A2, F3, D3, C3, G3, C3, G2,G2,G2,F2,F2,F2,E2,E2,E2,A2,A2,A2,G2,G2,G2,F2,F2,F2,B2,A2,C3,C3,C3, E3, D3, C3, C3, C3, G3, C3, A2, A2, A2, C3, C3,E3,G3,A3,A3,F3,D3,C3,G3,C3,C3] 
   bassDuration =  [QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, EN, EN, QN, EN ,EN, EN, EN, QN, EN ,EN, QN, QN, QN, QN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN ,EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, QN, QN, QN, QN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN]
   
   bassPitchOutro = [G2,G2,G2,F2,F2,F2,E2,E2,E2,A2,A2,A2,G2,G2,G2,F2,F2,F2,B2,A2,C3,C3,C3, E3, D3, C3, C3, C3, G3, C3, A2, A2, A2, C3, C3,E3,G3,A3,A3,F3,D3,C3,G3,C3,C3]
   bassDurationOutro = [QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, EN, EN, QN, EN, EN, QN, QN, QN, QN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN, EN, EN, QN]
   
   bassPitches = bassPitchOffset + 3 * bassPitch + bassPitchOutro
   bassDurations = bassDurationOffset + 3 * bassDuration + bassDurationOutro
   
   bass.addToPhase(bassPitches, bassDurations)  
   
   bass.create_score();
   
   # electGuitar
   electGuitar.addToPhase(pitches_intro, duration_intro)
   pitches =  [SILENT, A5, G5, E5, D5, D5, DS5, D5, C5, SILENT, E5, D5, SILENT]
   duration = [QN, DHN, WN, QN, DHN, SN, SN, DQN, DHN, HN, HN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, G5, E5, A5, E5, G5, SILENT, DS5, D5, C5, SILENT, C5, B4, A4, SILENT]
   duration =  [DHN, QN, SN, SN, SN, DHN, DEN, QN, QN, HN, EN, QN, QN, HN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [D4, DS4, E4, SILENT, A4, E4, G4, G4, SILENT, G4, A4, SILENT, D5, C5, SILENT]
   duration = [QN, QN, DHN, HN, QN, QN, HN, DQN, EN, QN, HN, QN, HN, HN, HN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches =  [D4, DS4, E4, SILENT, C5, D5, E5, G5, G5, SILENT, D6, C6, C6, SILENT, A5, E6, SILENT]
   duration = [QN, QN, DHN, QN, SN, SN, QN, EN, DHN, QN, DHN, QN, DQN, EN, QN, DHN, HN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [B5, A5, A5, G5, A5, B5, A5, A5, SILENT, A5, C6, D6, SILENT, D6, C6, E6, SILENT]
   duration = [DHN, QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, B5, A5, G5, A5, B5, G5, A5, G5, E5, D5, E5, DS5, A4, SILENT]
   duration = [QN, HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, HN, HN, HN, DHN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches =  [G5, E5, D5, D5, DS5, D5, C5, SILENT, E5, D5, SILENT]
   duration = [WN, QN, DHN, SN, SN, DQN, DHN, HN, HN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, G5, E5, A5, E5, G5, SILENT, DS5, D5, C5, SILENT, C5, B4, A4, SILENT]
   duration =  [DHN, QN, SN, SN, SN, DHN, DEN, QN, QN, HN, EN, QN, QN, HN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [B5, A5, A5, G5, A5, B5, A5, A5, SILENT, A5, C6, D6, SILENT, D6, C6, E6, SILENT]
   duration = [DHN, QN, QN, QN, QN, QN, QN, HN, QN, QN, QN, HN, QN, QN, QN, DHN, QN]
   electGuitar.addToPhase(pitches, duration)
   
   pitches = [A5, B5, A5, G5, A5, B5, G5, A5, G5, E5, D5, E5, DS5, A4, SILENT]
   duration = [QN, HN, HN, QN, QN, HN, HN, QN, QN, HN, HN, HN, HN, HN, HN]
   electGuitar.addToPhase(pitches, duration)
   electGuitar.create_score();
   # -------------------------------------------------
   
   # acGuitar
   firstchord = [[A3, E4, A4, C5, E5]]*5
   durationfirstchord = [QN, QN, QN, EN, EN]
   dynamicsfirstchord = [MP] * 5
   secondchord = [[G3, B3, E4, G4]] * 5
   durationsecondchord = [QN, QN, QN, EN, EN]
   dynamicssecondchord = [MP] * 5   
   
   acGuitar.addToPhase(pitches_intro, duration_intro, [MP])
   
   for i in range(30):
      acGuitar.addToPhase(firstchord,durationfirstchord,dynamicsfirstchord)
      acGuitar.addToPhase(secondchord,durationsecondchord,dynamicssecondchord)
   
   lastchord = [[A3, E4, A4, C5, E5], REST]
   duration = [HN]*2
   dynamics = [MP]*2
   acGuitar.addToPhase(lastchord, duration, dynamics)
   acGuitar.create_score()
   # -------------------------------------------------
   
   # piano
   pitches_intro =  [SILENT]
   duration_intro = [WN]   
   piano.addPhraseTwoHands(pitches_intro, duration_intro, pitches_intro, duration_intro)    
   
   r_pitches1 = [[A3, C4, E4],     [A3, C4, E4],      [A3, C4, E4],            [B3, E4, G4],     [B3, E4, G4], A3,      C4, E4]
   r_durations1 = [DQN,            DQN,                   QN,                     DQN,                QN,     EN,       EN, EN] 
   
   r_pitches2 = [[A3, C4, E4],     [A3, C4, E4],        [A3, C4, E4],         [B3, E4, G4],      [B3, E4, G4],         A4,G4]
   r_durations2 = [DQN,            DQN,                    QN,                    DQN,               DQN,              EN, EN]
     
   r_pitches3 = [[A3, C4, E4, A4], [A3, C4, E4, A4],        D4,DS4,              [B3, E4, G4],        [B3, E4, G4],    DS4,D4]
   r_durations3 = [DQN,            DQN,                     EN, EN,                  DQN,                 DQN,          EN, EN]     
   
   r_pitches4 = [[A3, C4, E4],     [A3, C4, E4],        [A3, C4, E4],         [B3, E4, G4],      [B3, E4, G4],       [B3, E4, G4],]
   r_durations4 = [DQN,            DQN,                    QN,                    DQN,               DQN,                QN,]
   
   r_pitches = r_pitches1 + r_pitches2 + r_pitches3 + r_pitches4
   r_durations = r_durations1 + r_durations2 + r_durations3 + r_durations4
   
   
   l_pitches1 = [[A1, A2],                    [A1, A2],           [A1, A2],             [E2, E3],           [E2, E3],            [E2, E3]]
   l_durations1 = [DQN,                         DQN,                 QN,                  DQN,                DQN,                  QN]    
   
   l_pitches2 = [ SILENT, [A1, A2],        SILENT,[A1, A2],       [A1, A2],         SILENT,[E2, E3],    SILENT,[E2, E3],       [E2, E3]]
   l_durations2 = [EN, QN,                 EN, QN,                  QN,                 EN, QN,             EN, QN,               QN]   
      
   l_pitches = 2 * l_pitches1 + l_pitches2 + l_pitches1
   l_durations = 2 * l_durations1 + l_durations2 + l_durations1
   
   piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations, 7)    
   piano.create_score(); 
   
   score.addPart(piano.l_hand_part)
   score.addPart(piano.r_hand_part)            
   score.addPart(acGuitar.part)
   score.addPart(electGuitar.part)
   score.addPart(drum.part)
   score.addPart(bass.part)
  
   Play.midi(score)   
   
#--------------INTERFACE PART-------------------------
d = Display("Interface", 800, 600)  #interface

#background color
rec1 = Rectangle(0, 0, 800, 600, Color(0, 120, 255), True)
d.add(rec1)

#tittle
title = Label("TTMP31") 
title.setFont(Font("SansSerif", Font.BOLD, 90))
d.add(title, 230,45)
d.getTitle()

#play button
rec1 = Rectangle(357, 282, 460, 320, Color.BLACK, True)
d.add(rec1)
playButton = Button("Play song", mainSong)
d.add(playButton, 365,290)

#volume
def printValue(volume):
   Play.setVolume(volume,0) 
   Play.setVolume(volume,1) 
   Play.setVolume(volume,2) 
   print(volume)
   
volume = VFader(490, 265, 510, 345, 0, 100, 50, printValue)
d.add(volume)


#instruments volumes
xPos = 130

def pianoVolume(newVolume):
   Play.setVolume(newVolume,0) 
   Play.setVolume(newVolume,1) 
pianoLabel = Label("Piano: ",LEFT,Color.WHITE)
pianoLabel.setFont(Font("Dialog", Font.BOLD, 16));
d.add(pianoLabel, 25,400)
pianoSlider = Slider(HORIZONTAL, 0, 100, 50, pianoVolume)
d.add(pianoSlider, xPos ,400)

def elecGuitarVolume(newVolume):
   Play.setVolume(newVolume,2)  
elecGuitarLabel = Label("Electric Guitar: ",LEFT,Color.WHITE)
elecGuitarLabel.setFont(Font("Dialog", Font.BOLD, 16));
d.add(elecGuitarLabel, 7,430)
elecGuitarSlider = Slider(HORIZONTAL, 0, 100, 50, elecGuitarVolume)
d.add(elecGuitarSlider, xPos ,430)

def acGuitarVolume(newVolume):
   Play.setVolume(newVolume,3) 
acGuitarLabel = Label("Acoustic Guitar: ",LEFT,Color.WHITE)
acGuitarLabel.setFont(Font("Dialog", Font.BOLD, 16));
d.add(acGuitarLabel, 5,460)
acGuitarSlider = Slider(HORIZONTAL, 0, 100, 50, acGuitarVolume)
d.add(acGuitarSlider, xPos,460)

def drumsVolume(newVolume):
   Play.setVolume(newVolume,4)  
drumsLabel = Label("Drums: ",LEFT,Color.WHITE)
drumsLabel.setFont(Font("Dialog", Font.BOLD, 16));
d.add(drumsLabel, 20,490)
drumsSlider = Slider(HORIZONTAL, 0, 100, 50, drumsVolume)
d.add(drumsSlider, xPos,490)

def bassVolume(newVolume):
   Play.setVolume(newVolume,5)
bassLabel = Label("Bass: ",LEFT,Color.WHITE)
bassLabel.setFont(Font("Dialog", Font.BOLD, 16));
d.add(bassLabel, 25,520)
bassSlider = Slider(HORIZONTAL, 0, 100, 50, bassVolume)
d.add(bassSlider, xPos,520)


#instruments checkboxes
xDPos = 600
pianoCheck = Checkbox("Piano")
d.add(pianoCheck, xDPos, 390)
pianoCheck.check()

bassCheck = Checkbox("Bass")
d.add(bassCheck, xDPos, 420)
bassCheck.check()

drumsCheck = Checkbox("Drums")
d.add(drumsCheck, xDPos, 450)
drumsCheck.check()

mGuitarCheck = Checkbox("Acoustic Guitar")
d.add(mGuitarCheck, xDPos, 480)
mGuitarCheck.check()

cGuitarCheck = Checkbox("Electric Guitar")
d.add(cGuitarCheck, xDPos, 510)
cGuitarCheck.check()

#download button
def downloadFunc():
   print("Downloading...")
   Write.midi(auxScore, "song.mid")
downloadBut = Button("Download song", downloadFunc)
d.add(downloadBut, xDPos, 550)