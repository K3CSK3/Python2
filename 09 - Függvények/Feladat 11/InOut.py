def inOutHour() -> int:
    num :int = None
    while (num == None):
        bevitel: str = None
        isNumber :bool = False
        bevitelCopy :str = None

        print("Adjon meg az óra számot: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(".", "").replace("-", "")
        isNumber = bevitelCopy.isnumeric()
        if (isNumber):
            num = int(bevitel)
        else:
            print("Nem számot adott meg!\n\n")
    return num

def inOutName() -> str:
    text :str = None
    while ((text == None) or (len(text) <= 2)):
        bevitel: str = None
        print("Adja meg a munkás nevét: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(" ", "")

        if (bevitelCopy.isalpha()):
            text = str(bevitel)
        else:
            print("Nem nevet adott meg!\n\n")
    return text

def kiiras(adat:str):
    print(adat)
    