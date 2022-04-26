# goldenTree.py
#
# Demonstrates how to draw a golden tree using recursion.
#
 
from gui import *
from math import *
 
# create display
d = Display("Golden Tree", 250, 250)
d.setColor(Color.WHITE)
 
# calculate phi to the highest accuracy Python allows
phi = (sqrt(5) - 1) / 2     # approx. 0.618033988749895
 
# recursive drawing parameters
depth = 11                  # amount of detail (or branching)
rotation = radians(60)      # branch angle is 60 degrees (need radians)
scale = phi                 # scaling factor of branches
 
# initial parameters
angle = radians(90)         # starting orientation is North
length = d.getHeight() / 3  # length of initial branch (trunk)
startX = d.getWidth() / 2   # start at bottom center
startY = d.getHeight() - 33
 
# recursive function for drawing tree
def drawTree(x, y, length, angle, depth):
   """
   Recursively draws a tree of depth 'depth' starting at 'x', 'y'.
   """
 
   global d, scale, rotation 
 
   #print "depth =", depth, "x =", x, " y =", y, " length =", length,
   #print "angle =", degrees(angle)
 
   # draw this line
   newX = x + length * cos( angle )    # calculate run
   newY = y - length * sin( angle )    # calculate rise
   d.drawLine(int(x), int(y), int(newX), int(newY))
 
   # check if we need more detail
   if depth > 1:
 
      # draw left branch - use line with length scaled by phi,
      # rotated counter-clockwise
      drawTree(newX, newY, length*phi, angle - rotation, depth-1)
 
      # draw right branch - use line with length scaled by phi,
      # rotated clockwise
      drawTree(newX, newY, length*phi, angle + rotation, depth-1)
 
# draw complete tree (recursively)
drawTree(startX, startY, length, angle, depth)