import random

def Gess_my_number():
  number = random.randint(1, 20)
  guess = int(input("I'm thinking of a number from 1 to 20. What is it? "))
  while guess != number:
    if guess < number:
      print("Your nummber is too low")
    else:
      print("Your number is to high")
    guess = int(input("pleas try again"))
  print("You did it")
  exit()
