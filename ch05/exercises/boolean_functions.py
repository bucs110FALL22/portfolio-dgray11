# Boolean Function Exercise
def percentage_to_letter(score=0):
  if score >= 90:
    return "A"
  if score >= 80 or score < 90:
    return "B"
  if score >= 70 or score < 80:
    return "C"
  if score >= 60 or score < 70:
    return "D"
  if score < 60:
    return "F"
    
perc = float(input("Please input a score: "))
  
a = percentage_to_letter(perc)

def is_passing(letter=None):
  if letter == "A" or letter == "B" or letter == "C":
    return True
  else:
    return False

print( is_passing(a) )






  