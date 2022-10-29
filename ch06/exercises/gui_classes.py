class box:
  def __init__(self):
    self.color = yellow
    self.inside_box = mushroom
    self.shape = square


class goomba:
  def __init__(self):
    self.height = 1
    self.speed = 1
    self.shape = goomba



class pipe:
    def __init__(self):
      self.color = green
      self.size = 2
      self.inside_box = nothing


class Background:
  def __init__(self):
    self.clouds = [] #cloud class
    self.color = "blue"
    self.random_blocks = True

class Player:
  def __init__(self):
    position = x, y
    image = "imagefile.png"
    score = 0