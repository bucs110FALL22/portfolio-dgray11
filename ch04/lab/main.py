import pygame
import random
import math



#PART A

pygame.init()
window = pygame.display.set_mode()

pygame.display.set_mode(size=(280,280))
window.fill("gray40")
pygame.display.flip()
#pygame.time.wait(5000)
print(pygame.display.get_window_size())

pygame.draw.circle(window, (255,255,255), (140,140), (140))
pygame.draw.line(window, (0,0,0), (0,140),(280,140))
pygame.draw.line(window, (0,0,0), (140,0),(140,280))
pygame.display.flip()
pygame.time.wait(2000)
team = True



# PART B

#throwing the darts
x1 = 140
y1 = 140
width = 280
pygame.display.flip()

for i in range(10):
  x2 = random.randrange(0,280)
  y2 = random.randrange(0,280)
  pygame.draw.circle(window, (0,0,0), (x2,y2), (2))
  pygame.display.flip()
  pygame.time.wait(1000)
  distance_from_center = math.hypot(x1-x2, y1-y2) #Distance formula
  is_in_circle = distance_from_center <= width/2 #Screen width
  print(is_in_circle)
  if not is_in_circle:
    pygame.draw.circle(window, (255,0,0), (x2,y2), (2))
  else:
    pygame.draw.circle(window, (0,255,0), (x2,y2), (2))
pygame.display.flip()
pygame.time.wait(3000)



#PART C

#Resetting the dart board
window = pygame.display.set_mode()
pygame.display.set_mode(size=(280,280))
window.fill("gray40")
pygame.draw.circle(window, (255,250,250), (140,140), (140))
pygame.draw.line(window, (0,0,0), (0,140),(280,140))
pygame.draw.line(window, (0,0,0), (140,0),(140,280))
pygame.display.flip()

while team == True:
  mouse_x, mouse_y = pygame.mouse.get_pos()
  red_box = pygame.draw.rect(window, (255,0,0), [10,245,25,25])
  blue_box = pygame.draw.rect(window, (0,0,255), [245,245,25,25])
  pygame.display.flip()
  pygame.time.wait(7000)

# Choosing a team
  print("select player RED or player BLUE")
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if blue_box.collidepoint(mouse_x, mouse_y):
        team = False
        print("Team is Blue")
      elif red_box.collidepoint(mouse_x, mouse_y):
        team = False
        print("Team is Red")

# Throwing the Darts
round = 1
red_pts = 0
blue_pts = 0
for i in range(10):
  print("ROUND", round)
  round = round + 1
  x2 = random.randrange(0,280)
  y2 = random.randrange(0,280)
  red = pygame.draw.circle(window, (0,0,0), (x2,y2), (2))
  pygame.display.flip()
  distance_from_center = math.hypot(x1-x2, y1-y2) #Distance formula
  is_in_circle = distance_from_center <= width/2 #Screen width
  if not is_in_circle:
    red = pygame.draw.circle(window, (255,0,0), (x2,y2), (2)) #red
    print("player1 misses!")
    pygame.time.wait(1000)
  else:
    pygame.draw.circle(window, (0,255,255), (x2,y2), (2)) #cyan
    print("player1 hits!")
    pygame.time.wait(1000)
    red_pts = red_pts + 1
  for i in range (1):
    x2 = random.randrange(0,280)
    y2 = random.randrange(0,280)
    blue = pygame.draw.circle(window, (0,0,0), (x2,y2), (2))
    distance_from_center = math.hypot(x1-x2, y1-y2) #Distance 
    is_in_circle = distance_from_center <= width/2 #Screen width
    if not is_in_circle:
      pygame.draw.circle(window, (255,0,255), (x2,y2), (2)) #magenta
      print("player2 misses!")
      pygame.time.wait(1000)
    else:
      pygame.draw.circle(window, (0,255,0), (x2,y2), (2)) #green
      print("player2 hits!")
      pygame.time.wait(1000)
      blue_pts = blue_pts + 1
pygame.display.flip()
pygame.time.wait(3000)

# Determining whether your team won or not
for i in range(1):
  if red_box.collidepoint(mouse_x, mouse_y):
    if red_pts > blue_pts: 
      print("YAY, red team won!")
    elif red_pts < blue_pts:
      print("AWW MAN, red team lost!")
    else:
      print("TIE!!!")
  if blue_box.collidepoint(mouse_x, mouse_y):
    if blue_pts > red_pts: 
      print("YAY, blue team won!")
    elif blue_pts < red_pts:
      print("AWW MAN, blue team lost!")
    else:
      print("It's a tie!!!")