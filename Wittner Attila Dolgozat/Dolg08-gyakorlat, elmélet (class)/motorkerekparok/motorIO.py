import os
from motor import Motor
from typing import *

def faljBeolvasas(fajlnev) -> List[Motor]:

    osszesMotor: List[Motor] = []

    alapUt = os.path.dirname(os.path.abspath(__file__))
    teljesUt = os.path.join(alapUt,fajlnev)
    try:
        with open(file=teljesUt, encoding="utf-8", mode="r") as fajl:
            for sor in fajl:
                egyMotor: Motor = Motor()
                adat = sor.replace("\n", "").split("\t")
                egyMotor.gyarto = adat[0]
                egyMotor.modell = adat[1]
                egyMotor.gyartasiEv = int(adat[2])
                egyMotor.ar = int(adat[3])

                osszesMotor.append(egyMotor)

    except FileNotFoundError as ex:
        print(f"A fájl {ex.filename} nem található vagy nem létezik")
    
    
    return osszesMotor

def fajlbaIras(fajlnev, motorok):

    alapUt = os.path.dirname(os.path.abspath(__file__))
    teljesUt = os.path.join(alapUt,fajlnev)

    try:
        with open(file=teljesUt, encoding="utf-8", mode="w") as fajl:
            for motor in motorok:
                fajl.write(f"{motor}")

    except FileNotFoundError as ex:
        print(f"A fájl {ex.filename} nem található vagy nem létezik")
