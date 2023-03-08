szam :int = 0
bevitel :str = None

while (szam <= 100):
    print("Adjon meg egy számot (minimum 3 jegyűt): ", end="")
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        if (szam < 100):
            print("A szám legyen nagyobb 100-nál")
        szam = int(bevitel)
        if (szam % 7 == 0):
            print("Osztható 7-el")
        else:
            print("Nem osztható 7-el")
    else:
        print("Nem számot adott meg!\n\n")