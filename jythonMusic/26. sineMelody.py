# sineMelody.py
#
# This program demonstrates how to create a melody from a sine wave.
# It maps the sine function to a melodic (i.e., pitch) contour.
#
 
from music import *
from math import *  
 
phr = Phrase()
density = 25.0                 # higher for more notes in sine curve
cycle = int(2 * pi * density)  # steps to traverse a complete cycle
 
# create one cycle of the sine curve at given density
for i in range(cycle):
   value = sin(i / density)    # calculate the next sine value
   pitch = mapValue(value, -1.0, 1.0, C2, C8)   # map to range C2-C8
   note = Note(pitch, TN)
   phr.addNote(note)
# now, all the notes have been created
 
View.pianoRoll(phr)  # so view them
Play.midi(phr)       # and play them