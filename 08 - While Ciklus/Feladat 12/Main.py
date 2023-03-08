takaritottPenz :int = 0
bevitel :str = None
szerzettPenz :int = 0
honap :int = 0

while (takaritottPenz <= 0):
    print("Adja meg a megtakarított pénz mennyiségét: ",end='')
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        takaritottPenz = int(bevitel)
    else:
        print("Nem számot adott meg")

szerzettPenz = takaritottPenz
while (szerzettPenz < 100000):
    szerzettPenz += szerzettPenz * 0.02
    honap += 1
print(f"Az ön pénze({bevitel}) {honap} hónap alatt érné el a 100.000-et 2%-os kamattal")