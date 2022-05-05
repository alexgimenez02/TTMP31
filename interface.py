from music import *
from gui import *


def mainSong():
   print "Now the music would play..."
   #MAIN COMPOSITION
   

#INTERFACE PART
d = Display("Interface", 1000, 700)  #interface

title = Label("TTMP31") 
title.setFont(Font("Dialog", Font.BOLD, 50))
d.add(title, 350,10)
d.getTitle()

rec1 = Rectangle(397, 312, 500, 350, Color.BLACK, True)
d.add(rec1)
playButton = Button("Play song", mainSong)
d.add(playButton, 405,320)

def printValue(volume):
   print volume   # replace this with whatever needs to happen
volume = VFader(575, 300, 595, 380, 0, 100, 50, printValue)
d.add(volume)


#checkboxs
pianoCheck = Checkbox("Piano")
d.add(pianoCheck, 50, 310)
pianoCheck.check()

pianoCheck = Checkbox("Bass")
d.add(pianoCheck, 50, 340)
pianoCheck.check()

pianoCheck = Checkbox("Drums")
d.add(pianoCheck, 50, 370)
pianoCheck.check()

pianoCheck = Checkbox("Main Guitar")
d.add(pianoCheck, 50, 400)
pianoCheck.check()

pianoCheck = Checkbox("Complementary Guitar")
d.add(pianoCheck, 50, 430)
pianoCheck.check()

def downloadFunc():
   print("Downloading...")
downloadBut = Button("Download song", downloadFunc)
d.add(downloadBut, 610,530)