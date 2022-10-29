def foo(message, num = 1):
  print(message * num)


foo('Welcome')
foo('Viewers', 3)

class Point:
  def __init__(self, x=0, y=0, color="red"):
    self.x = x
    self.y = y
    if color == "green":
      print("You are a bad person")
      color = "blue"
    self.color = color

p1 = Point() #initialize a Point object
print(p1.x, p1.y, p1.color, type(p1))
p2 = Point(x=5, y=2, color="green") #initialize another Point object
print(p2.x, p2.y, p2.color, type(p2))