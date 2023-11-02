def code_incripter():
  go = "YES"
  while go != "NO":
    print(
      "-----------RESTART--------------RESTART----------------RESTART----------"
    )

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ "
    stringtoencrypt = input("please enter a message to encrypt:")
    stringtoencrypt = stringtoencrypt.upper()
    shiftamountstr = input(
      "Please enter a whole number from 1-25 to be your key.")
    try:
      shiftamount = int(shiftamountstr)
    except:
      print("a whole number.")
      exit()
    encrypyrdstring = ""
    for currentcharacter in stringtoencrypt:
      position = alphabet.find(currentcharacter)
      newposition = position + shiftamount
      if currentcharacter in alphabet:
        encrypyrdstring = encrypyrdstring + alphabet[newposition]
      else:
        encrypyrdstring = encrypyrdstring + alphabet[newposition]
      #print(" your encrypted new message is", encrypyrdstring)
    print(
      "---------------------------------------------------------------------")
    print()
    print(" Your message is", stringtoencrypt)
    print(" your encrypted message is", encrypyrdstring)
    print()
    print(
      "--------------------------------------------------------------------")
    go = input("Press enter to to start again, or type No to leave").upper()