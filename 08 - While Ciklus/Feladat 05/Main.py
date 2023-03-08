szam :int = None
hatar :int = 0
osszeg :int = 0
bevitel :str = None


while (hatar < 100):
    print("Adjon meg egy határ értéket (min 100): ",end="")
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        hatar = float(bevitel)
    else:
        print("Nem számot adott meg!")


while (osszeg < 100):
    print("Adjon meg egy számot: ",end="")
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        szam = float(bevitel)
        osszeg += szam
    else:
        print("Nem számot adott meg!")
    print(osszeg)