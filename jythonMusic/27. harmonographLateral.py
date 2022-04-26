# harmonographLateral.py
#
# Demonstrates how to create a lateral (2-pendulum) harmonograph
# in Python.
#
# See Ashton, A. (2003), Harmonograph: A Visual Guide to the
# Mathematics of Music, Wooden Books, p.19.
#
 
from gui import *
from math import *
 
d = Display("Lateral Harmonograph", 250, 250)
centerX = d.getWidth() / 2    # find center of display
centerY = d.getHeight() / 2
 
# harmonograph parameters
freq1 = 2   # holds frequency of first pendulum
freq2 = 3   # holds frequency of second pendulum
ampl  = 50  # the distance each pendulum swings
 
density = 50                   # higher for more detail
cycle = int(2 * pi * density)  # steps to traverse a complete cycle
times = 6                      # how many cycles to run
 
# display harmonograph ratio setting
d.drawText("Ratio " + str(freq1) + ":" + str(freq2), 95, 20)
 
# go around the unit circle as many times requested
for i in range(cycle * times):
 
   # get angular position on unit circle (divide by a float
   # for more accuracy)
   rotation = i / float(density)  
 
   # get x and y coordinates (run and rise)
   x = sin( rotation * freq1 ) * ampl   # get run (same phase)
   #x = cos( rotation * freq1 ) * ampl   # get run (opposite phase)
   y = sin( rotation * freq2 ) * ampl   # get rise
 
   # convert to display coordinates (move display origin to center,
   # from top-left)
   x = x + centerX
   y = y + centerY
 
   # draw this point (pixel coordinates are int)
   d.drawPoint( int(x), int(y) )