import turtle
import random

t = turtle.Turtle()
window = turtle.Screen()
t.shape("turtle")
t.speed(1)

distance = 15
angle = 90
is_in_screen = True

colors = ["green", "blue", "purple"]

while is_in_screen:
  coin = random.randrange(0,2)
  if coin == 0:
    t.left(angle)
  else:
    t.right(angle)
  t.forward(distance)

  turtleX = t.xcor()
  turtleY = t.ycor()

  x_range = window.window_width()/2
  y_range = window.window_height()/2

  t.color(colors[0])

  colors.append(colors.pop(0))

  if abs(turtleX) > x_range or abs(turtleY) > y_range:
    is_in_screen = False

window.bgcolor("blue")
window.exitonclick()


  






