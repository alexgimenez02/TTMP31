from music import *
from gui import *


def mainSong():
   print "Now the music would play..."
   #MAIN COMPOSITION
   

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
   print volume   # replace this with whatever needs to happen
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
downloadBut = Button("Download song", downloadFunc)
d.add(downloadBut, 610,530)