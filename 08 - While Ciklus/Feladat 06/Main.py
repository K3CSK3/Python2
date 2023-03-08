eletkor :int = -1
bevitel :str = None

while (eletkor < 0 or eletkor > 100):
    print("Adjon meg az életkorát (0-99): ",end="")
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        eletkor = float(bevitel)
    else:
        print("Nem számot adott meg!")




if (eletkor >= 0 and eletkor <= 6):
    print("gyerek")
elif (eletkor >= 7 and eletkor <= 18):
    print("iskolás")
elif (eletkor >= 19 and eletkor <= 64):
    print("dolgozó")
elif (eletkor >= 65):
    print("nyugdíjas")