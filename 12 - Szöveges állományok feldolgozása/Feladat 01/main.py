from typing import *
from tanuloIO import *
from modell.tanulo import *
from atlag import *
from legnagyobbAtlag import *
from atlagFelett import *
from filebaIras import *
from kitunoTanulo import *


tanulok :List[Tanulo] = tanuloBekeres()

# 1. Feladat --- Tanulók Kiírása
print("OSztály Tanulói")
for line in tanulok:
    print(line)


# 2. Feladat --- Osztály Létszám Kiírása
osztalyLetszam: int = len(tanulok)
print(f"\n\nAz osztályban {osztalyLetszam} tanuló jár\n\n")


# 3. Feladat --- Osztály Átlag Kiírása
osztalyAtlag = atlagSzamito(tanulok)
print(f"az osztaly atlag {osztalyAtlag}")


# 4. Feladat --- Legnagyobb Átlag Kiírása
legnagyobbAtlag = legnagyobbAtlagKereso(tanulok)
print(f"Az osztályban a legnagyobb átlag:\n{legnagyobbAtlag}")


# 5. Feladat --- Átlag Felletti Tanulók Kiírása Fájlba
atlagFelettiek = atlagFelettiTanulok(tanulok, osztalyAtlag)
kiirasFileba(atlagFelettiek, "atlagfelettiek.txt")


# 6. Feladat --- Kitűnő Tanulók Kiírása
vanKitunoTanulo = kitunoTanulo(tanulok)

if vanKitunoTanulo: # if legnagyobbAtlag == 5.00:
    print("VAN kitűnő tanuló az osztályban!")
else:
    print("NINCS kitűnő tanuló az osztályban!")