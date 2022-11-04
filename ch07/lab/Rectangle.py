class Rectangle:
  def __init__(self, x, y, height, width):
    self.x = x
    if self.x < 0:
      self.x = 0
    self.y = y
    if self.y < 0:
      self.y = 0
    self.height = height
    if self.height < 0:
      self.height = 0
    self.width = width
    if self.width < 0:
      self.width = 0
    
    
  def __str__(self):
    output = "(x:{}, y:{}, height:{}, width:{}".format(self.x,self.y,self.height,self.width)  
    return(output)

    # result_str = f"{self.x}"
    # result_str += f"{self.y}"
    # result_str += f"{self.height}"
    # result_str += f"{self.width}"
    # return result_str