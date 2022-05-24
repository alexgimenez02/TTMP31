from music import *
from gui import *
from piano import Piano
from electricguitar import electricGuitar

pianoSelected = True
electGuitarSelected = True
score  = Score("Composition", 120)

def mainSong():
   #MAIN COMPOSITION
   print "Playing..."
   piano = Piano("Piano test", 120, [0, 1])
   electGuitar = electricGuitar("Electric guitar", 120, 2)   
   
   pitches = [SILENT, A5,     G5,      E5, D5,     D5, DS5, D5, C5]
   duration = [QN,    DHN,    WN,      QN, DHN,    SN, SN, DQN, DHN ]   
   electGuitar.addToPhase(pitches, duration)
   electGuitar.create_score();
   
   r_pitches = [[A3, C4, E4], [A3, C4, E4], [A3, C4, E4],     [B3, E4, G4], [B3, E4, G4], [B3, E4, G4]]
   r_durations = [DQN,            DQN,            QN,              DQN,          DQN,           QN] 
   l_pitches = [[A1, A2],        [A1, A2],     [A1, A2],         [E2, E3],    [E2, E3],      [E2, E3]]
   l_durations = [DQN,             DQN,           QN,                DQN,        DQN,           QN]    
   piano.addPhraseTwoHands(l_pitches, l_durations, r_pitches, r_durations, 2)    
   piano.create_score();   
   
   if pianoCheck.isChecked():
      score.addPart(piano.l_hand_part)
      score.addPart(piano.r_hand_part)   
   if cGuitarCheck.isChecked():
      score.addPart(electGuitar.part)   
   Play.midi(score)   
   

#--------------INTERFACE PART-------------------------
d = Display("Interface", 1000, 700)  #interface

#tittle
title = Label("TTMP31") 
title.setFont(Font("Dialog", Font.BOLD, 50))
d.add(title, 350,10)
d.getTitle()

#play button
rec1 = Rectangle(397, 312, 500, 350, Color.BLACK, True)
d.add(rec1)
playButton = Button("Play song", mainSong)
d.add(playButton, 405,320)

#volume
def printValue(volume):
   Play.setVolume(volume,0) 
   Play.setVolume(volume,1) 
   Play.setVolume(volume,2) 
   print(volume)
   #Mod.normalize(volume)   # replace this with whatever needs to happen
volume = VFader(575, 300, 595, 380, 0, 100, 50, printValue)
d.add(volume)


#instruments checkboxes
pianoCheck = Checkbox("Piano")
d.add(pianoCheck, 50, 310)
pianoCheck.check()

bassCheck = Checkbox("Bass")
d.add(bassCheck, 50, 340)
bassCheck.check()

drumsCheck = Checkbox("Drums")
d.add(drumsCheck, 50, 370)
drumsCheck.check()

mGuitarCheck = Checkbox("Main Guitar")
d.add(mGuitarCheck, 50, 400)
mGuitarCheck.check()

cGuitarCheck = Checkbox("Complementary Guitar")
d.add(cGuitarCheck, 50, 430)
cGuitarCheck.check()

#download button
def downloadFunc():
   print("Downloading...")
   Write.midi(score, "song.mid")
downloadBut = Button("Download song", downloadFunc)
d.add(downloadBut, 610,530)