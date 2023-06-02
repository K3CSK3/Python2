from Jatekos import *
from JatekosIO import *
from funkciok import *

"""
A roplabda.txt állományban az adatok a következő módón vannak tárolva:
Név,
Magasság,
Poszt,
Nemzetiség,
Csapat,
Ország (ahol a csapat játszik)

- Írjuk ki a képernyőre az össz adatot
- Keressük ki az ütő játékosokat az utok.txt állömányba
- A csapattagok.txt állományba mentsük a csapatokat és a hozzájuk tartozó játékosokat a következő formában:
  Telekom Baku: Yelizaveta Mammadova,Yekaterina Gamova,
- Rendezzük a játékosokat magasság szerint növekvő sorrendbe és a magaslatok.txt állományba mentsük el.
- Mutassuk be a nemzetisegek.txt állományba, hogy mely nemzetiségek képviseltetik magukat a röplabdavilágban mint játékosok és milyen számban.
- atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.
- Állítsa növekvő sorrendbe a posztok szerint a játékosok ösz magasságát
- Egy szöveges állományba, „alacsonyak.txt” keresse ki a játékosok átlagmagasságától alacsonyabb játékosokat. Az állomány tartalmazza a játékosok nevét,  magasságát és hogy mennyivel alacsonyabbak az átlagnál, 2 tizedes pontossággal.
"""



jatekosok: list[Jatekos]= fajlBeolvasas("adatok.txt")

jatekosKiiras(jatekosok)

posztKereso(jatekosok, "ütő")

fajlbaIras(jatekosok, "utok.txt")