def Times_mashen():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    table = int(input("Please type a times table: "))
    number = int(input("Up to: "))
    for x in range(0, number + 1):
      print(x, "x", table, "=", x * table)
    editchoice = input(
      "Press return to play again, or type EXIT to leave. ").upper()
    if editchoice == "EXIT":
      exit()
