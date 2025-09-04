def checkChar(c):
    if(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        print("Alphabet")
    elif(c in "1234567890"):
        print("Digit")
    else:
        print("Special Character")
checkChar("A")