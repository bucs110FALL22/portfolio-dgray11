import turtle

window = turtle.Screen()



num_sides = int(input("enter number of sides: "))
length_sides = int(input("enter length: "))

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

angle = 360 / num_sides
for i in [angle]*num_sides:
  my_turtle.forward(length_sides)
  my_turtle.left(i)

window.exitonclick()