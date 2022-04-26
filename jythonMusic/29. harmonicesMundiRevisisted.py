# harmonicesMundiRevisisted.py
#
# Sonify mean planetary velocities in the solar system.
#
 
from music import *
from math import *
from random import *
 
# Create a list of planet mean orbital velocities
# Mercury, Venus, Earth, Mars, Ceres, Jupiter, Saturn, Uranus,
# Neptune. (Ceres is included in place of the 5th missing planet
# as per Bode's law).
planetVelocities = [47.89, 35.03, 29.79, 24.13, 17.882, 13.06, 9.64,
                    6.81, 5.43]
numNotes     = 100       # number of notes generated per planet
durations    = [SN, QN]  # a choice of durations
instrument   = EPIANO    # instrument to use
speedFactor  = 0.01      # decrease for slower sound oscillations
 
score = Score(60.0)      # holds planetary sonification
 
# get minimum and maximum velocities:
minVelocity = min(planetVelocities)
maxVelocity = max(planetVelocities)
 
# define a function to create one planet's notes - returns a Part
def sonifyPlanet(numNotes, planetIndex, durations, planetVelocities):
   """Returns a part with a sonification of a planet's velocity."""
 
   part = Part(EPIANO, planetIndex)   # use planet index for channel
   phr = Phrase(0.0)
 
   planetVelocity = planetVelocities[planetIndex]   # get velocity 
 
   # create all the notes by tracing the oscillation generated using
   # the planetary velocities
   for i in range(numNotes):
 
      # pitch is constant
      pitch = mapScale(planetVelocity, minVelocity, maxVelocity,
                       C3, C6, MIXOLYDIAN_SCALE, C4)
 
      # panning and dynamic oscillate based on planetary velocity
      pan = mapValue(sin(i * planetVelocity * speedFactor * 2),
                     -1.0, 1.0, PAN_LEFT, PAN_RIGHT)
      dyn = mapValue(cos(i * planetVelocity * speedFactor * 3),
                     -1.0, 1.0, 40, 127)
 
      # create the note and add it the the phrase
      n = Note(pitch, choice(durations), dyn, pan)
      phr.addNote(n)
 
   # now, all notes have been created
 
   part.addPhrase(phr)  # add phrase to part
   return part          # and return it
 
# iterate over all plants
for i in range( len(planetVelocities) ):
   part = sonifyPlanet(numNotes, i, durations, planetVelocities)
   score.addPart(part)
 
View.sketch(score)
Play.midi(score)