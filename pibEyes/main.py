#!/usr/bin/python3

from p5 import *
# From the file "innereye.py" import the class "Eye"
from innereye import Eye

# Variables for pib eyes
eyeball = 400
iris = 350
pupil = 280
big_light = 50
small_light = 30

current_color = Color(0, 159, 227) # blue eyes for initialisation

def setup():
  # Put code to run once here
  #size(1024, 600) # width and height
  size(1280, 720) # width and height
  
  noStroke()
  global el, er
  el = Eye( width/4, height/2)
  er = Eye( 3*width/4, height/2)

def eyes_opened():
  # Display left eye (inner eye centered)
  el.display()

  # Display right eye (inner eye centered)
  er.display()
  
def eyes_closed():
  # Display closed eyes (two rounded rectangles)
  noStroke()
  fill(255, 255, 255)
  
  # closed left eye
  ellipse(width/4 - eyeball/2 + big_light/2, height/2, big_light, big_light)
  ellipse(width/4 + eyeball/2 - big_light/2, height/2, big_light, big_light)
  rect(width/4 - eyeball/2 + big_light/2, height/2 - big_light/2, eyeball - big_light, big_light)
  
  # closed right eye
  ellipse(3*width/4 - eyeball/2 + big_light/2, height/2, big_light, big_light)
  ellipse(3*width/4 + eyeball/2 - big_light/2, height/2, big_light, big_light)
  rect(3*width/4 - eyeball/2 + big_light/2, height/2 - big_light/2, eyeball - big_light, big_light)

def draw():
  background(0, 0, 0) # reset the drawing every frame
  global current_color

  # Calculate the current color based on the frame count
  if frame_count <= 150:
      current_color = Color(
          lerp(0, 230, frame_count / 150),
          lerp(159, 0, frame_count / 150),
          lerp(227, 126, frame_count / 150)
      )
  elif frame_count <= 300:
      current_color = Color(
          lerp(230, 149, (frame_count - 150) / 150),
          lerp(0, 27, (frame_count - 150) / 150),
          lerp(126, 129, (frame_count - 150) / 150)
      )
  
  if mouse_is_pressed:
      eyes_closed() # if mouse is pressed, the eyes will close
  elif mouse_x > width/4+eyeball/2 and mouse_x < 3*width/4-eyeball/2 and mouse_y > height/2-eyeball/4 and mouse_y < height/2+eyeball/4:
      # nothings happening, when mouse is between the eyes (in small rectangle)
      # Display left eye (inner eye centered)
      el.display(current_color)

      # Display right eye (inner eye centered)
      er.display(current_color)
  else:
      # update eyes by following mouse position
      el.update(mouse_x, mouse_y) # update left eye and copy transformation on right eye
      el.displayLeft(current_color) # display both eyes (based on left eye)
  
  
# Keep this to run your code
run()
