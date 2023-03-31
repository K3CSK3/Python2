def InOut() -> int:
    num :int = None
    while (num == None):
        bevitel: str = None
        isNumber :bool = False
        bevitelCopy :str = None

        bevitel = input()
        bevitelCopy = bevitel.replace(".", "").replace("-", "")
        isNumber = bevitelCopy.isnumeric()
        if (isNumber):
            num = int(bevitel)
        else:
            print("Nem számot adott meg!\n\n")
    return num