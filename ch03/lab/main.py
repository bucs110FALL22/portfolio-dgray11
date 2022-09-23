import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.screensize(2000,2000) ###
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


## 5. Your PART A code goes here
#1
michelangelo.speed(0.6)
leonardo.speed(0.6)
x = random.randrange(1,100)
y = random.randrange(1,100)
michelangelo.forward(x)
leonardo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
#2
for i in range(10):
  w = random.randrange(1,100)
  z = random.randrange(1,100)
  michelangelo.forward(w)
  leonardo.forward(z)
  window.delay(25)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

# EQUILATERAL TRIANGLE
window.fill("blueviolet")
pygame.display.flip()
pygame.time.wait(500)

coords = []
num_sides = 3
side_length = 70
offset = 100

for i in range (num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x,y)
  coords.append(points)
polygon = pygame.draw.polygon(window, ("pink"), coords)
pygame.display.flip()
pygame.time.wait(2500)

# SQUARE
window.fill("blueviolet")
pygame.display.flip()
pygame.time.wait(500)

coords2 = []
num_sides2 = 4
side_length = 70
offset = 100

for i in range (num_sides2):
  theta = (2.0 * math.pi * (i)) / num_sides2
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x,y)
  coords2.append(points)
polygon = pygame.draw.polygon(window, ("pink"), coords2)
pygame.display.flip()
pygame.time.wait(2500)

# HEXAGON
window.fill("blueviolet")
pygame.display.flip()
pygame.time.wait(500)

coords3 = []
num_sides3 = 6
side_length = 70
offset = 100

for i in range (num_sides3):
  theta = (2.0 * math.pi * (i)) / num_sides3
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x,y)
  coords3.append(points)
polygon = pygame.draw.polygon(window, ("pink"), coords3)
pygame.display.flip()
pygame.time.wait(2500)

# NONAGON
window.fill("blueviolet")
pygame.display.flip()
pygame.time.wait(500)

coords4 = []
num_sides4 = 9
side_length = 70
offset = 100

for i in range (num_sides4):
  theta = (2.0 * math.pi * (i)) / num_sides4
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x,y)
  coords4.append(points)
polygon = pygame.draw.polygon(window, ("pink"), coords4)
pygame.display.flip()
pygame.time.wait(2500)

# CIRCLE
window.fill("blueviolet")
pygame.display.flip()
pygame.time.wait(500)

coords5 = []
num_sides5 = 360
side_length = 70
offset = 100

for i in range (num_sides5):
  theta = (2.0 * math.pi * (i)) / num_sides5
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x,y)
  coords5.append(points)
polygon = pygame.draw.polygon(window, ("pink"), coords5)
pygame.display.flip()
pygame.time.wait(2500)






window.exitonclick()

#to add to a list
#coords.append(X,Y)
