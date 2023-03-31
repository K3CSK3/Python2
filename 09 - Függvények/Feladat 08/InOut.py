def InOut() -> str:
    koordX :int = None

    while (koordX == None):
        bevitel: str = None
        isNumber :bool = False
        bevitelCopy :str = None
        print("Adjon meg a pont X koordinátáját: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(".", "").replace("-", "")
        isNumber = bevitelCopy.isnumeric()
        if (isNumber):
            koordX = float(bevitel)
        else:
            print("Nem számot adott meg!\n\n")


    koordY :int = None
    while (koordY == None):
        bevitel: str = None
        isNumber :bool = False
        bevitelCopy :str = None
        print("Adjon meg a pont Y koordinátáját: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(".", "").replace("-", "")
        isNumber = bevitelCopy.isnumeric()
        if (isNumber):
            koordY = float(bevitel)
        else:
            print("Nem számot adott meg!\n\n")

    koordinata = str(koordX) + ";" + str(koordY)
    return koordinata

def kiiras(adat:str)-> None:
    print(f"A két pont {adat} távolságra van")