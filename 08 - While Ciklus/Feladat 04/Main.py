szam :int = None
osszeg :int = 0
bevitel :str = None

print("Adjon meg egy számot: ",end="")
bevitel = input()
osszeg = szam

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