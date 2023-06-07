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

- atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.

- Egy szöveges állományba, „alacsonyak.txt” keresse ki a játékosok átlagmagasságától alacsonyabb játékosokat. Az állomány tartalmazza a játékosok nevét,  magasságát és hogy mennyivel alacsonyabbak az átlagnál, 2 tizedes pontossággal.
"""

jatekosok: list[Jatekos]= fajlBeolvasas("adatok.txt")

jatekosKiiras(jatekosok)

utok = posztKereso(jatekosok, "ütő")
fajlbaIras(utok, "utok.txt")


magassag = jatekosok
magassagRendezo(magassag, "növekvő")
fajlbaIras(magassag, "magaslatok.txt")

atlagnalMagasabbak = atlagnalMagasagabb(jatekosok)
fajlbaIras(atlagnalMagasabbak, "atlagnalmagasabbak.txt")

atlagtolKisebbek = atlagtolKisebb(jatekosok)
fajlbaIras(atlagtolKisebbek, "alacsonyak.txt")