class StringUtility:
  def __init__(self, string):
    def vowels(self):
      count = 0
      vowel = set("aeiouAEIOU")
      for i in str:
        if i in vowel:
          count = count + 1
          print("number of vowels is", count)
        elif count > 5:
          print("many")
        
    def bothEnds(self):
      if len(self) < 2:
        return ""
      return self[0:2] + self[-2:]
      
    def fixStart(self):
      # char = self[0]
      # length = len(self)
      # s = self.replace(char, "*")
      # s = char + self[1:]
      # return s

      return self[0] + self[1:].replace(self[0], '*')
       
    def asciiSum(self):
      # ???
    #   for i in num:
    #     add += ord(self)
      list = []
      for i in list:
        ascii_sum = 0
        ascii_sum += ord(self)
        
    def cipher(self):
    #   length = len(self)
    #   self(ord(self) + length)
      for i in range(0, len(self)):
        self += ord(self)
  def __str__(self):
    return self