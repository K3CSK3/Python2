from InOut import *
import random

def randomSzam() -> str:
    szam1 = random.randrange(0,10)
    szam2 = random.randrange(40,51)
    randomNum = random.randrange(szam1, szam2)
    output = str(szam1) + ";" + str(szam2) + ";" + str(randomNum)
    return output

def tipp(input:str) -> None:
    bevitel = 0
    probakSzama :int = 0
    szam1 = int(input.split(";")[0])
    szam2 = int(input.split(";")[1])
    randomNum = int(input.split(";")[2])

    while (bevitel != randomNum):
        probakSzama += 1
        print(f"Eddig ennyiszer tippeltél:{probakSzama}")
        print(f"Gondoltam egy számra {szam1} és {szam2} között: ",end='')
        bevitel = InOut()
        if (bevitel > randomNum):
            print("A kitalálandó szám kisebb")
        if (bevitel < randomNum):
            print("A kitalálandó szám nagyobb")

        if (bevitel == randomNum):
            print("Kitaláltad!")
        else:
            print("Nem találtad el!")
