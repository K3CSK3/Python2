def InOut() -> float:
    num :float = None
    while (num == None):
        bevitel: str = None
        isNumber :bool = False
        bevitelCopy :str = None

        print("Adjon meg egy számot: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(".", "").replace("-", "")
        isNumber = bevitelCopy.isnumeric()
        if (isNumber):
            num = float(bevitel)
        else:
            print("Nem számot adott meg!\n\n")
    return num