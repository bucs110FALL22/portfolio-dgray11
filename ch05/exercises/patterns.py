# Part 1
def star_pyramid():
  print("Please input a number of lines")
  lines = int(input())
  star = str("*")
  for i in range(1, lines + 1):
      star = i * str("*")
      print(star)

star_pyramid()


# Part 2
def rstar_pyramid():
  print("Please input a number of lines")
  rlines = int(input())
  rstar = str("*")
  for i in range(rlines, 0, -1):
      rstar = i * str("*")
      print(rstar)

rstar_pyramid()










