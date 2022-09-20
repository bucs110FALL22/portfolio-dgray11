import random

# for i in range(1, 10):
#   num =  int(input(“Enter a number between 1 and 10: ”))
#   if num < i
#   print("too low")

# num = random.randrange(1, 11)

# num_guesses = 0

# for i in range(5):
#   guess_num = int(input("Please enter a guess: "))
#   #num_guesses = num_guesses + 1
#   num_guesses += 1
#   if guess_num > num:
#     print("your guess is too high")
#   elif guess_num < num:
#     print("your guess is too low")
#   else:
#     print("Correct!")

# print("it took you", num_guesses, "to get it right")




num = random.randrange(1, 11)
num_guesses = 0
correct_guess = False

for i in range(11):
  if not correct_guess:
      guess_num = int(input("please enter a guess:"))
    #num_guesses = num_guesses + 1
      num_guesses += 1
      if guess_num > num:
        print("your guess is too high")
      elif guess_num < num:
        print("your guess is too low")
      else:
        print("Correct!")
        correct_guess = True

        if guess_num == num:
          break
          #this ends the loop
print("it took you", num_guesses, "to get it right")