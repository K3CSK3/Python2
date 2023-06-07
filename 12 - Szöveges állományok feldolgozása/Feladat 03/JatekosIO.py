import os
from Jatekos import *

def fajlBeolvasas(filenev) -> list[Jatekos]:

    jatekosok :list[Jatekos] = []

    alapUt = os.path.dirname(__file__) + "/data/"
    teljesUt = os.path.join(alapUt,filenev)

    try:
        with open(file=teljesUt,encoding="utf8",mode="r") as file:
            osszAdat = file.readlines()
            for line in osszAdat:
                adat = line.strip().split("\t")
                jatekos: Jatekos = Jatekos()
                jatekos.nev = adat[0]
                jatekos.magassag = adat[1]
                jatekos.poszt = adat[2]
                jatekos.nemzetiseg = adat[3]
                jatekos.csapat = adat[4]
                jatekos.orszag = adat[5]
                jatekosok.append(jatekos)
        return jatekosok
    except FileNotFoundError as ex:
        print(f"A fájl nem létezik vagy nem található {ex.filename}")
        return []

def fajlbaIras(jatekosok:list[Jatekos], filenev) -> None:

    alapUt = os.path.dirname(__file__) + "/output/"
    teljesUt = os.path.join(alapUt,filenev)

    try:
        with open(file=teljesUt,encoding="utf8",mode="w") as file:
            for jatekos in jatekosok:
                file.write(f"{jatekos}\n")
    except FileNotFoundError as ex:
        print(f"A fájl nem létezik vagy nem található {ex.filename}")


def jatekosKiiras(jatekosok: list[Jatekos]):
    print("\nRöplabdások:\n")
    for jatekos in jatekosok:
        print(f"{str(jatekos)}\n")