def elsoInOut() -> str:
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
    return text

def masodikInOut() -> str:
    text2 :str = None
    while (text2 == None):
        print("Adjon meg még egy szót: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(" ", "")
        if ((len(bevitel) >= 2) and (bevitelCopy.isalpha())):
            text2 = str(bevitel)
        else:
            print("Nem szót adott meg!\n\n")
    return text2

def kiiras(text01:str, text02:str, egyezik:int) -> None:
    print(f"Ebben a két szóban {text01}, {text02} {egyezik} betű egyezik")