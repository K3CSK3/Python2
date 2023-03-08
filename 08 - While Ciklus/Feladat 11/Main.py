import random

parosSzam :int = 1
paratlanSzam :int = 2
bevitel :str = None
tavolsagParos :int = 0
tavolsagParatlan :int = 0
mennyiseg :int = 0 
osszeg :int = 0
atlag :int = 0
ciklusKezdes :int = 0
neggyelOszthato :int = 0
kozelebb :str = None



while (parosSzam %2 != 0):
    print("Adjon meg egy páros számot: ",end='')
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        parosSzam = int(bevitel)
    else:
        print("Nem számot adott meg")



while ((paratlanSzam %2 != 1) or paratlanSzam < parosSzam):
    print("Adjon meg egy nagyobb páratlan számot: ",end='')
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        paratlanSzam = int(bevitel)
    else:
        print("Nem számot adott meg")


randomSzam = random.randrange(parosSzam, paratlanSzam)

tavolsagParos = randomSzam - parosSzam
tavolsagParatlan = paratlanSzam - randomSzam

if (tavolsagParos < tavolsagParatlan):
    kozelebb = "PÁROS"
else:
    kozelebb = "PÁRATLAN"


for i in range(parosSzam, paratlanSzam+1, 1):
    osszeg += i
    mennyiseg += 1
atlag = osszeg/mennyiseg


ciklusKezdes = parosSzam + parosSzam % 4
for i in range(ciklusKezdes, paratlanSzam + 1, 4):
    neggyelOszthato += 1

print(f"A random szám({randomSzam}) a {kozelebb}-hoz van közelebb,\n köztük({parosSzam},{paratlanSzam}) lévő átlag: {atlag}\n a néggyel osztható számok mennyisége: {neggyelOszthato}")