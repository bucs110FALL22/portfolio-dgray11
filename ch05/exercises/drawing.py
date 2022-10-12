import turtle

window = turtle.Screen()

def drawEqShape(myturtle=None, num_sides=0, side_length=0):
  for i in range(num_sides):
    myturtle.left(360 / num_sides)
    myturtle.forward(side_length)
	
leo = turtle.Turtle()
leo.shape("turtle")
leo.color("green")

num_sides = int(input("number of sides: "))
side_length = int(input("side length: "))

drawEqShape(leo, num_sides, side_length)

window.exitonclick()