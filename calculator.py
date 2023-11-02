def Couclator():
  question = input(" + - X / ")
  if question == "x":
    Times()
  elif question == "-":
    Sutract()
  elif question == "/":
    devide()
  elif question == "+":
    pluss()


def pluss():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    a = int(input())
    b = int(input())
    answer = a + b
    print(a, "+", b, "=", answer)
    editchoice = input(
      "Press return to carry on, or type EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()


def devide():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    a = int(input())
    b = int(input())
    answer = a / b
    print(a, "/", b, "=", answer)
    editchoice = input(
      "Press return to carry on, or type EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()


def Sutract():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    a = int(input())
    b = int(input())
    answer = a - b
    print(a, "-", b, "=", answer)
    editchoice = input(
      "Press return to carry on, or type EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()


def Times():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    a = int(input())
    b = int(input())
    answer = a * b
    print(a, "x", b, "=", answer)
    editchoice = input(
      "Press return to carry on, or type EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()
