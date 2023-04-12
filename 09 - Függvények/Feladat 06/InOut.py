def numInOut() -> float:
    num :float = None
    while (num == None):
        bevitel: str = None
        isNumber :bool = False
        bevitelCopy :str = None
        print("Adjon meg egy hőfok értéket: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(".", "").replace("-", "")
        isNumber = bevitelCopy.isnumeric()
        if (isNumber):
            num = float(bevitel)
        else:
            print("Nem hőfokot adott meg!\n\n")
    return num

def textInOut() -> str:
    text :str = None
    bevitel: str = None
    while (text == None):
        print("Adja meg melyék mértékegségbe váltson a program (Kelvin/Farenheit): ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(" ", "")
        if (("K" in bevitelCopy) and (bevitelCopy.isalpha())):
            text = "K"
        elif (("F" in bevitelCopy) and (bevitelCopy.isalpha())):
            text = "F"
        else:
            print("Nem jót adott meg!\n\n")
    return text.upper()

def kiiras(tipus:str, ertek:float, mennyiseg:float) -> None:
    if tipus == "K":
        print(f"{ertek} C° {mennyiseg} Kelvin lesz")
    elif tipus == "F":
        print(f"{ertek} C° {mennyiseg} Farenheit lesz")