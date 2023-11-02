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
    anser = a + b
    print(a, "+", b, "=", anser)
    editchoice = input(
      "press return to carry on, or type EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()


def devide():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    a = int(input())
    b = int(input())
    anser = a / b
    print(a, "/", b, "=", anser)
    editchoice = input(
      "press return to carry on, or type EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()


def Sutract():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    a = int(input())
    b = int(input())
    anser = a - b
    print(a, "-", b, "=", anser)
    editchoice = input(
      "press return to carry on, or type EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()


def Times():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    a = int(input())
    b = int(input())
    anser = a * b
    print(a, "x", b, "=", anser)
    editchoice = input(
      "press return to carry on, or type EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()