from linecache import getline
from tkinter import Label, Entry, Tk, Button
import bombdodger
import code_encrypter
import aliens
import calculator
import timesTables
import guessmynumber
import tictactoe
import random_story_cube

from random import randint as r


def IsYourNumberRandom():
  Z = r(1, 50)
  A = 0
  X = int(input("Enter a random number between 1 and 50 "))
  seeGuesses = input("Do you want to see the computer's guesses? ")
  if X > 50 or X < 1:
    print("Try again")
    X = int(input("Enter a random number between 1 and 50 "))
  while X != Z:
    if seeGuesses.lower() == "yes" or seeGuesses.lower() == "y":
      print(Z)
    Z = r(1, 50)
    A = A + 1
    if X == Z:
      print("It took the computer", A, "tries to guess your number")


def gamesSubmitCommand():
  global gamesInput
  global Gamesroot
  gameChoice = gamesInput.get()
  Gamesroot.destroy()
  if gameChoice == "bombdodger":
    bombdodger.play()
  elif gameChoice == "calculator":
    calculator.Couclator()
  elif gameChoice == "tic tac toe":
    print("tic tac toe")
    TicTacToe()
  elif gameChoice == "guess my number":
    Gess_my_number()
  elif gameChoice == "times tables":
    timesTables.Times_mashen()
  elif gameChoice == "story":
    print()
    random_story_cube()
  elif gameChoice == "encrypter":
    pasword3 = input("password")
    if pasword3 == "C0DE":
      code_encrypter.code_incripter()
    else:
      print("Stop tring to hack us")
      exit()
  elif gameChoice == "aliens":
    print()
    aliens.alions()
  elif gameChoice == "is your number random":
    IsYourNumberRandom()
  else:
    print("We do not have that game")
    selectGame()


def selectGame():
  games = [
    "Bombdodger", "Encrypter", "Aliens", "Calculator", "Times tables",
    "Guess my number", "Tic Tac Toe", "Story", "Is Your Number Random"
  ]
  gamesLength = len(games)
  gamesString = "Games: " + ', '.join(
    games[0:gamesLength - 1]) + " or " + games[gamesLength - 1]
  global Gamesroot
  Gamesroot = Tk()
  Gamesroot.title("Pick a game")
  gamesLabel = Label(Gamesroot, text=gamesString)
  gamesLabel.grid(row=0, column=0, columnspan=300)
  global gamesInput
  gamesInput = Entry(Gamesroot)
  gamesInput.grid(row=1, column=0)
  gamesSubmit = Button(Gamesroot, text="submit", command=gamesSubmitCommand)
  gamesSubmit.grid(row=2, column=0)


a = 1
infoFound = False


def checkLines(stringA):
  global a
  global infoFound
  line = getline(r"passwords.txt", a)
  if line == stringA:
    hoorayLabel = Label(root, text="Signed in")
    hoorayLabel.grid(row=4, column=0)
    root.destroy()
    selectGame()
    infoFound = True
  else:
    a = a + 1
    if a > 50:
      infoFound = False
      return
    checkLines(string)


def signUp():
  SignUpLabel = Label(
    root, text="We have signed you up because you \n didn't have an account")
  SignUpLabel.grid(row=4, column=0, columnspan=2)
  print("Login again to see games")


def appendNew():
  global a
  global username
  global password
  global root
  file = open("passwords.txt", 'a')
  usrnm = "UserName: " + username
  pwd = "Password: " + password
  global string
  string = usrnm + pwd + "\n"
  checkLines(string)
  if infoFound == False:
    file.write(string)
    signUp()
  file.close


root = Tk()
root.title("Sign in/up")

nameLabel = Label(root, text="Name: ")
nameLabel.grid(row=0, column=0)

nameInput = Entry(root)
nameInput.grid(row=0, column=1)

passLabel = Label(root, text="Password: ")
passLabel.grid(row=1, column=0)

passInput = Entry(root)
passInput.grid(row=1, column=1)


def submit():
  global username
  username = nameInput.get()
  with open("signedinuser.txt", "w") as file:
    file.write(username)
  global password
  password = passInput.get()
  appendNew()

submit = Button(root, text="Submit", command=submit)
submit.grid(row=3, column=0)

root.mainloop()
