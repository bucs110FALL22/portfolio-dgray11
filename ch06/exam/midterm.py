import turtle

window = turtle.Screen()
window.bgcolor("green")
window.screensize(1000,1000)

leo = turtle.Turtle()
leo.shape("turtle")
leo.color("pink")

# main function that draws the staircase
def main(the_turtle=None, size_of_stair=0):
  print("How many stairs should the staircase have? (recommended 5)")
  stairs = int(input())
  for i in range(stairs):
    leo.left(90)
    leo.forward(size_of_stair)
    leo.right(90)
    leo.forward(size_of_stair)
  base_and_side(size_of_stair, stairs)
  
# function that finds the length of the staircase and draws the base and side of the staircase
def base_and_side(length_of_stair, stairs):
  result = 0
  for i in range(2):
    leo.right(90)
    leo.forward(length_of_stair * stairs)
  return result

# Making the drawing
main(leo, 20)

window.exitonclick()