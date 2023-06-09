"""
Futási példa:


e) feladat
adatok kiírva az olocso-draga.txt állományba
"""

from motor import Motor
from motorIO import *
from funkciok import *
from typing import *

# A program olvassa be és tárolja el az adatok.txt fájlban lévő motorkerékpárok adatait egy annak megfelelő adatszerkezetbe! (3)
motorok: List[Motor] = faljBeolvasas("adatok.txt")

# Állapítsa meg, hány motorkerékpár adatait kell feldolgozni! Az eredményt a mintának megfelelően írja ki! (1)
# a) feladat
# 23 motorkerékpár adatait dolgozzuk fel.
adathossz = adatMennyisegKereso(motorok)
print(f"{adathossz} motorkerékpár adatait dolgozzuk fel.")

# Állapítsa meg, hány motorkerékpárt gyártottak 2000 után! Az eredményt a mintának megfelelően írja ki! (1)
# b) feladat
# 11 motorkerékpárt gyártottak 2000 után
ev = 2000
darab = evUtanGyartottak(motorok, ev)
print(f"{darab} motorkerékpárt gyártottak {ev} után")

# Írja ki a mintának megfelelően a motorkerékpárok árainak átlagát két tizedes pontossággal! Az eredményt a mintának megfelelően írja ki!  (2)
# c) feladat
# 3522,60EUR a motorkerékpárok árainak átlaga
arakAtlaga = arAtlag(motorok)
print(f"{arakAtlaga}EUR a motorkerékpárok árainak átlaga")

# Melyik a legöregebb motorkerékpár? Az eredményt a mintának megfelelően írja ki!  (3)
# d) feladat
# A legidősebb motorkerékpár a Ural IMZ M72 (1957)
legidosebb: List[Motor] = legidosebbMotor(motorok)
print(f"A legidősebb motorkerékpár a {legidosebb.gyarto} {legidosebb.modell} {legidosebb.gyartasiEv}")

# Rakja növekvő sorrendbe a motorkerékpárokat az ár tulajdonságuk szerint és írja ki az adatokat az olocso-draga.txt szöveges file-ba! (5)
sorbaRakas(motorok)
fajlbaIras("olocso-draga.txt",motorok)
