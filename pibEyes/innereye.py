#!/usr/bin/python3

from p5 import *

# Variables for pib eyes
eyeball = 400
iris = 350
pupil = 280
big_light = 50
small_light = 30



class Eye(object):
  angle = 0.0 # global class variable
  
  def __init__(self, xpos, ypos):
    global eyeball, iris, pupil, big_light, small_light
    self.xpos = xpos
    self.ypos = ypos
  
  def display(self, c):
    # eyeball
    fill(255, 255, 255)
    ellipse(self.xpos, self.ypos, eyeball, eyeball)    
    
    # iris
    #fill(105, 190, 190) # turquoise    
    fill(c)
    ellipse(self.xpos, self.ypos, iris, iris)
  
    # pupil
    fill(0, 0, 0)
    ellipse(self.xpos, self.ypos, pupil, pupil)
  
    # lightpoints
    fill(255, 255, 255)
    ellipse(self.xpos + 70, self.ypos - 50, big_light, big_light)
    ellipse(self.xpos + 20, self.ypos - 20, small_light, small_light)
    
  def update(self, mx, my):
      global angle
      angle = atan2(my-self.ypos, mx-self.xpos) 

  def displayLeft(self, c):           
      # basic eye, here: left
      pushMatrix()
      translate(self.xpos, self.ypos)
      
      # eyeball left
      fill(255, 255, 255)
      ellipse(0, 0, eyeball, eyeball)
      
      rotate(angle)
    
      # iris
      #fill(105, 190, 190) # turquoise      
      fill(c)
      ellipse(self.xpos/13, 0, iris, iris)
      # pupil
      fill(0, 0, 0)
      ellipse(self.xpos/13, 0, pupil, pupil)
      
      popMatrix()
      
      # lightpoints left
      fill(255, 255, 255)
      ellipse(self.xpos + 70, self.ypos - 50, big_light, big_light)
      ellipse(self.xpos + 20, self.ypos - 20, small_light, small_light)
      
      
      # display other eye, here: right
      pushMatrix()
      translate(self.xpos + width/2, self.ypos)
      
      # eyeball left
      fill(255, 255, 255)
      ellipse(0, 0, eyeball, eyeball)
      
      rotate(angle)
      
      # iris
      #fill(105, 190, 190) # turquoise      
      fill(c)
      ellipse(self.xpos/13, 0, iris, iris)
      # pupil
      fill(0, 0, 0)
      ellipse(self.xpos/13, 0, pupil, pupil)
      
      popMatrix()
      
      # lightpoints right
      fill(255, 255, 255)
      ellipse(3*self.xpos + 70, self.ypos - 50, big_light, big_light)
      ellipse(3*self.xpos + 20, self.ypos - 20, small_light, small_light)
