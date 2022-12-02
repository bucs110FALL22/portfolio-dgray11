class StringUtility:
  
  def __init__(self, string):
    self.string = string

  """
  returns the internal string itself
  """
  def __str__(self):
    return self.string

  """
  counts the number of vowels in the string, and returns a new string where <count> is the number of vowels in the string as a string 
  """
  def vowels(self):
    count = 0
    vowel = set("aeiouAEIOU")
    for i in self.string:
      if i in vowel:
        count = count + 1
        print("number of vowels is", count)
      elif count > 5:
        print("many")
    
  """
  returns a string made of the first 2 and last 2 chars of the original string
  if the string length is less than or equal to 2, return an empty string instead    
  """
  def bothEnds(self):
    if len(self) < 2:
      return ""
    else: string = (self.string[0] + self.string[1] + self.string[-2] + self.string[1])
    return(string)
    
      #return self[0:2] + self[-2:]

  """
  returns a string where all occurrences of its first char have been changed to '*'
  does not change the first char itself
  """
  def fixStart(self):
    if len(self.string) == 0:
      return(self.string)
    replaceString = self.string[0]
    string = self.string
    for i in self.string:
      if i == replaceString:
        string = string.replace(i,"*")
      string = string.replace("*", replaceString, 1)
      
    # char = self[0]
    # s = self.replace(char, "*")
    # s = char + self[1:]
    # return s

    #length = len(self)
    #return self[0] + self[1:].replace(self[0], '*')

    """
    returns an integer that is the sum of all ascii values in the string
    """
    def asciiSum(self):
      string = self.string
      sum = 0
      for i in string:
        sum = sum + ord(i)
      # ???
    #   for i in num:
    #     add += ord(self)
      # list = []
      # for i in list:
      #   ascii_sum = 0
      #   ascii_sum += ord(self)
    
    """
    returns an encoded string by incrementing all letters by the length of the string
    """
    def cipher(self):
      lowercase_a = 97
      uppercase_a = 65
      lowercase_z = 122
      uppercase_z = 90
      lowermax = 149
      uppermax = 92

      string = self.string
      cipher = ""
      shift = len(string)
      for char in string:
        value = ord(char)
        if(value >= uppercase_a and value <= uppercase_z):
          if(value + shift) > uppercase_z:
            cipher = chr((uppercase_a -1) + ((value + shift) % uppercase_z))
          else:
            cipher = string + chr(value + shift)
        elif (value >= lowercase_a and value <= lowercase_z):
          if(value + shift) > lowercase_z:
            cipher = chr((lowercase_a -1) + ((value + shift) % lowercase_z))
          else:
            cipher += string + chr(value + shift)








        
      #     c = ord(char)
      #     if (c >= ord("A") and c <= ord("Z")):
      #         cipher += chr((c - ord("A") + 1) % 26 + ord("A"))
      #     elif (c >= ord("a") and c <= ord("z")):
      #         cipher += chr((c - ord("a") + 1) % 26 + ord("a"))
      #     else: cipher += char
      
      # return cipher



      
      # cipher = ""
      # for i in self.string:
      #   #if i = isalpha():
      #     alphabet = ord(i) + len(self.string)
      #     if i > ord("z"):
      #       alphabet -= 26
      #     letter = chr(alphabet)
      #     cipher += letter
      # return cipher



      
    #   length = len(self)
    #   self(ord(self) + length)
      # for i in range(0, len(self)):
      #   self += ord(self)
        
 