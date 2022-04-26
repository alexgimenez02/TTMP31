# harmonographRotary.py
#
# Demonstrates how to create a rotary (3-pendulum) harmonograph
# in Python.
#
# Here, the position of the pen is determined by two pendula,
# and is modeled by either (sin, sin) or (cos, sin).
# The third pendulum has its own sin() and cos() to model the second
# circle.
#
# See Ashton, A. (2003), Harmonograph: A Visual Guide to the
# Mathematics of Music, Wooden Books, p.19.
#
 
from gui import *
from math import *
 
d = Display("Rotary Harmonograph", 250, 250)
centerX = d.getWidth() / 2    # find center of display
centerY = d.getHeight() / 2
 
# harmonograph parameters
freq1 = 2     # holds frequency of first pendulum
freq2 = 3     # holds frequency of second pendulum
ampl1 = 40    # holds swing of movement for pair of pendulums
              # (radius of first circle)
 
ampl2 = ampl1 # holds swing of movement for third pendulum
              # (radius of second circle)
 
#friction = 0.0003   # how much energy is lost per iteration
 
density = 50                  # higher for more detail
cycle = int(2 * pi * density)  # steps to traverse a complete cycle
times = 1                      # how many cycles to run
 
# display harmonograph ratio setting
d.drawText("Freq Ratio " + str(freq1) + ":" + str(freq2), 80, 10)
 
# go around the unit circle as many times requested
for i in range(cycle * times):
 
   # get angular position on unit circle (divide by a float
   # for more accuracy)
   rotation = i / float(density)  
 
   # get x and y coordinates (run and rise)
   x1 = sin( rotation * freq1 ) * ampl1  # get run (same phase)
   y1 = cos( rotation * freq1 ) * ampl1   # get rise
   #x1 = cos( rotation * freq1 ) * ampl1  # get run (opposite phase)
   #y1 = sin( rotation * freq1 ) * ampl1   # get rise
 
   x2 = sin( rotation * freq2) * ampl2   # get run (second pendulum)
   y2 = cos( rotation * freq2) * ampl2   # get rise
 
   # combine the two oscillations
   x = (x1 - x2)
   y = (y1 - y2)
 
   # convert to display coordinates (move display origin to center,
   # from top-left)
   x = x + centerX
   y = y + centerY
 
   # draw this point (pixel coordinates are int)
   d.drawPoint( int(x), int(y) )  
 
   # loss some energy due to friction
#   ampl1 = ampl1 * (1 - friction)
#   ampl2 = ampl2 * (1 - friction)