def InOut() -> str:
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
            
    return text