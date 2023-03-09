def InOut() -> str:
    text :str = None
    bevitel: str = None
    while (text == None):
        print("Adjon meg egy szót: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(" ", "")

        if ((len(bevitel) >= 2) and (bevitelCopy.isalpha())):
            text = str(bevitel)
        else:
            print("Nem szót adott meg!\n\n")
        
    text2 :str = None
    while (text2 == None):
        print("Adjon meg még egy szót: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(" ", "")
        if ((len(bevitel) >= 2) and (bevitelCopy.isalpha())):
            text2 = str(bevitel)
        else:
            print("Nem szót adott meg!\n\n")
            
    return [text, text2]