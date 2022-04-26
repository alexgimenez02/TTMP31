# sierpinskiTriangle.py
#
# Demonstrates how to draw the Sierpinski triangle using recursion.
#
 
from gui import *
 
# create display
d = Display("Sierpinski Triangle", 250, 250)
#d.setColor(Color.WHITE)
 
# recursive drawing parameters
depth = 6      # amount of detail (number of subdivisions) 
 
# initial points
x      = d.getWidth() / 2    # top corner
y      = 20
width  = d.getWidth() - 40
height = d.getHeight() - y - 30
 
# recursive function for drawing triangle
def drawTriangle(x, y, width, height, depth):
   """
   Recursively draws a Sierpinski triangle of depth 'depth' with top at 'x', 'y', and
   provided 'width' and 'height'.
   """
   global d  # display to draw tree
 
   # get corners
   x1, y1 = x, y                     # top
   x2, y2 = x - width/2, y + height  # left
   x3, y3 = x + width/2, y + height  # right
 
   # reached the pixel level?
   if depth == 1:
 
      d.drawPolygon([x1, x2, x3], [y1, y2, y3])   # yes, so draw a triangle
 
   else:   # no, so continue subdividing
 
      # get top corners of subtriangles
      topX, topY     = x, y
      leftX, leftY   = x - width/4, y + height/2
      rightX, rightY = x + width/4, y + height/2
 
      # and draw them recursively
      drawTriangle(topX, topY, width/2, height/2, depth-1)      # draw top subtriangle
      drawTriangle(leftX, leftY, width/2, height/2, depth-1)    # draw left subtriangle
      drawTriangle(rightX, rightY, width/2, height/2, depth-1)  # draw right subtriangle
 
# draw complete Sierpinski triangle (recursively)
drawTriangle(x, y, width, height, depth)