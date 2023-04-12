from InOut import *
import random

def jatek(randomNum:int) -> None:
    tipp = 0
    probakSzama :int = 0
    
    while (tipp != randomNum):
        probakSzama += 1
        print(f"Eddig ennyiszer tippeltél:{probakSzama}")
        print(f"Gondoltam egy számra: ",end='')
        tipp = InOut()
        if (tipp > randomNum):
            print("A kitalálandó szám kisebb")
        if (tipp < randomNum):
            print("A kitalálandó szám nagyobb")

        if (tipp == randomNum):
            print("Kitaláltad!")
        else:
            print("Nem találtad el!")
