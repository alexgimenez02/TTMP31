# boids.py
#
# This program simulates 2D boid behavior.
#
# See http://www.red3d.com/cwr/boids/ and
# http://www.vergenet.net/~conrad/boids/pseudocode.html
#
 
from gui import *
from math import *
from random import *
 
# universe parameters
universeWidth  = 1000   # how wide the display
universeHeight = 800    # how high the display
 
# boid generation parameters
numBoids   = 200        # from 2 to as much as your CPU can handle
boidRadius = 2          # radius of boids
boidColor  = Color.BLUE # color of boids
 
# boid distance parameters
minSeparation  = 30     # min comfortable distance between two boids
flockThershold = 100    # boids closer than this are in a local flock
 
# boid behavior parameters (higher means quicker/stronger)
separationFactor = 0.01 # how quickly to separate
alignmentFactor = 0.16  # how quickly to align with local flockmates
cohesionFactor = 0.01   # how quickly to converge to attraction point
frictionFactor = 1.1    # how hard it is to move (dampening factor)
 
### define boid universe, a place where boids exist and interact ####
class BoidUniverse:
   """This is the boid universe, where boids exist and interact.
      It is basically a GUI Display, with boids (moving Circles)
      added to it.  While boids are represented as circles, they
      have a little more logic to them - they can sense where other
      boids are, and act accordingly.  While individual boids have
      simple rules for sensing their environment and reacting,
      very intricate, complex, naturally-looking patterns of behavior
      emerges, similar to those of birds flying high in the sky
      (among others).  The rules of behavior are the same for all
      boids, and are defined in the Boid class (a sister class to
      this one).
   """
 
   def __init__(self, title = "", width = 600, height = 400,
                frameRate=30):
 
      self.display = Display(title, width, height) # universe display
 
      self.boids = []                              # list of boids
 
      # holds attraction point for boids (initially, universe center)
      self.attractPoint = complex(width/2, height/2)  
 
      # create timer
      delay = 1000 / frameRate     # convert frame rate to delay (ms)
      self.timer = Timer(int(delay), self.animate)       # animation timer
 
      # when mouse is dragged, call this function to set the
      # attraction point for boids
      self.display.onMouseDrag( self.moveAttractionPoint )
 
   def start(self):
      """Starts animation."""
      self.timer.start()   # start movement!
 
   def stop(self):
      """Stops animation."""
      self.timer.stop()    # stop movement
 
   def add(self, boid):
      """Adds another boid to the system."""
 
      self.boids.append( boid )          # remember this boid
      self.display.add( boid.circle )    # add a circle for this boid
 
   def animate(self):
      """Makes boids come alive."""
 
      ### sensing and acting loop for all boids in the universe !!!
      for boid in self.boids:   # for every boid
 
         # first observe other boids and decide how to adjust movement
         boid.sense(self.boids, self.attractPoint)   
 
         # and then, make it so (move)!
         boid.act(self.display)                      
 
   def moveAttractionPoint(self, x, y):
      """Update the attraction point for all boids."""
      self.attractPoint = complex(x, y)
 
### define the boids, individual agents who can sense and act #######
class Boid:
   """This a boid.  A boid is a simplified bird (or other species)
      that lives in a flock.  A boid is represented as a circle,
      however, it has a little more logic to it - it can sense where
      other boids are, and act, simply by adjusting its direction of
      movement.  The new direction is a combination of its reactions
      from individual rules of thumb (e.g., move towards the center
      of the universe, avoid collisions with other boids, fly in the
      same general direction as boids around you (follow the local
      flock, as you perceive it), and so on.  Out of these simple
      rules intricate, complex behavior emerges, similar to that of
      real birds (or other species) in nature.
   """
 
   def __init__(self, x, y, radius, color,
                initVelocityX=1, initVelocityY=1 ):
      """Initialize boid's position, size, and initial
         velocity (x, y).
      """
 
      # a boid is a filled circle
      self.circle = Circle(x, y, radius, color, True) 
 
      # set boid size, position
      self.radius = radius                # boid radius
      self.coordinates = complex(x, y)    # boid coordinates (x, y)
 
      # NOTE: We treat velocity in a simple way, i.e., as the
      # x, y displacement to add to the current boid coordinates,
      # to find where to move its circle next.  This moving is done
      # once per animation frame.
 
      # initialize boid velocity (x, y)
      self.velocity = complex(initVelocityX, initVelocityY)  
 
   def sense(self, boids, center):
      """
      Sense other boids' positions, etc., and adjust velocity
      (i.e., the displacement of where to move next).
      """
 
      # use individual rules of thumb, to decide where to move next
 
      # 1. Rule of Separation - move away from other flockmates
      #                         to avoid crowding them
      self.separation = self.rule1_Separation(boids)
 
      # 2. Rule of Alignment - move towards the average heading
      #                        of other flockmates
      self.alignment = self.rule2_Alignment(boids)
 
      # 3. Rule of Cohesion - move toward the center of the universe
      self.cohesion = self.rule3_Cohesion(boids, center)
 
      # 4. Rule of Avoidance: move to avoid any obstacles
      #self.avoidance = self.rule4_Avoidance(boids)
 
      # create composite behavior
      self.velocity = (self.velocity / frictionFactor) + \
                      self.separation + self.alignment + \
                      self.cohesion            
 
   def act(self, display):
      """Move boid to a new position using current velocity."""
 
      # Again, we treat velocity in a simple way, i.e., as the
      # x, y displacement to add to the current boid coordinates,
      # to find where to move its circle next.
 
      # update coordinates
      self.coordinates = self.coordinates + self.velocity
 
      # get boid (x, y) coordinates
      x = self.coordinates.real  # get the x part
      y = self.coordinates.imag  # get the y part
 
      # act (i.e., move boid to new position)
      display.move( self.circle, int(x), int(y) )
 
   ##### steering behaviors ####################
   def rule1_Separation(self, boids):
      """Return proper velocity to keep separate from other boids,
         i.e., avoid collisions.
      """
 
      newVelocity = complex(0, 0)  # holds new velocity
 
      # get distance from every other boid in the flock, and as long
      # as we are too close for comfort, calculate direction to
      # move away (remember, velocity is just an x, y distance
      # to travel in the next animation/movement frame)
      for boid in boids:           # for each boid
 
         separation = self.distance(boid)   # how far are we?
 
         # too close for comfort (excluding ourself)?
         if separation < minSeparation and boid != self:
            # yes, so let's move away from this boid
            newVelocity = newVelocity - \
                          (boid.coordinates - self.coordinates)
 
      return newVelocity * separationFactor  # return new velocity
 
   def rule2_Alignment(self, boids):
      """Return proper velocity to move in the same general direction
         as local flockmates.
      """
 
      totalVelocity = complex(0, 0) # holds sum of boid velocities
      numLocalFlockmates = 0        # holds count of local flockmates
 
      # iterate through all the boids looking for local flockmates,
      # and accumuate all their velocities
      for boid in boids:
 
         separation = self.distance(boid)    # get boid distance
 
         # if this a local flockmate, record its velocity
         if separation < flockThershold and boid != self:                      
            totalVelocity = totalVelocity + boid.velocity             
            numLocalFlockmates = numLocalFlockmates + 1       
         
      # average flock velocity (excluding ourselves)       
      if numLocalFlockmates > 0:
         avgVelocity = totalVelocity / numLocalFlockmates
      else:
         avgVelocity = totalVelocity
 
      # adjust velocity by how quickly we want to align
      newVelocity = avgVelocity - self.velocity
 
      return newVelocity * alignmentFactor  # return new velocity
 
   def rule3_Cohesion(self, boids, center):
      """Return proper velocity to bring us closer to center of the
         universe.
      """
 
      newVelocity = center - self.coordinates
 
      return newVelocity * cohesionFactor  # return new velocity
 
   ##### helper function ####################
   def distance(self, other):
      """Calculate the Euclidean distance between this and
         another boid.
      """
 
      xDistance = (self.coordinates.real - other.coordinates.real)
      yDistance = (self.coordinates.imag - other.coordinates.imag)
 
      return sqrt( xDistance*xDistance + yDistance*yDistance )
 
# start boid simulation
universe = BoidUniverse(title="Boid Flocking Behavior",
                        width=universeWidth, height=universeHeight,
                        frameRate=30)
 
# create and place boids
for i in range(0, numBoids):
 
   # get random position for this boid
   x = randint(0, universeWidth)
   y = randint(0, universeHeight)
 
   # create a boid with random position and velocity
   boid = Boid(x, y, boidRadius, boidColor, 1, 1)
   universe.add( boid )
 
# animate boids
universe.start()