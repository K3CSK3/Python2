def InOut() -> int:
    num :int = None
    while (num == None):
        bevitel: str = None
        isNumber :bool = False
        bevitelCopy :str = None

        print("Adja meg a születési évét: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(".", "").replace("-", "")
        isNumber = bevitelCopy.isnumeric()
        if (isNumber):
            num = int(bevitel)
        else:
            print("Nem egy évet adott meg!\n\n")

            
    text :str = None
    while (text == None):
        bevitel: str = None
        print("Adjon meg a nevét: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(" ", "")
        if ((len(bevitel) >= 2) and (bevitelCopy.isalpha())):
            text = str(bevitel)
        else:
            print("Nem nevet adott meg!\n\n")
    return [text,num]