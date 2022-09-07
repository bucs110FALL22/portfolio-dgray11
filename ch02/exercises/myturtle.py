import turtle
window = turtle.Screen()

my_turtle = turtle.Turtle()
my_turtle.color("purple")
my_turtle.shape("turtle")

length = 50
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)

my_turtle.right(90)
my_turtle.up()
my_turtle.forward(length)
my_turtle.down()
my_turtle.color("red")

my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)
my_turtle.forward(length)
my_turtle.left(90)

window.exitonclick()

#num_slides = int(input("enter number of sides: "))
#length = 50
#angle = 360 / num_sides
#for i in [angle]*num_sides:
#my_turtle.forward(length)
#my_turtle.left(i)
#window.exitonclick()


  