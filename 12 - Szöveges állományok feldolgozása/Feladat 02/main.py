from konyvIO import *
from modell.konyv import Konyvek
from funkciók import *


#Írjuk ki a képernyőre az össz adatot
konyvek: list[Konyvek] = konyvBeolvasas("adatok.txt")
for konyv in konyvek:
    print(konyv)

#Keressük ki az informatika témajú könyveket és mentsük el őket az informatika.txt állömányba
infosKonyvek: list[Konyvek] = temaKereses(konyvek, "informatika")
fajlbaIras(infosKonyvek,"informatika.txt")

#Az 1900.txt állományba mentsük el azokat a könyveket amelyek az 1900-as években íródtak
megfeleloSzazadbanMegjelentKonyvek: list[Konyvek] = evjaratSzamitas(konyvek, 1900, 2000)
fajlbaIras(megfeleloSzazadbanMegjelentKonyvek, "1900.txt")

#Rendezzük az adatokat a könyvek oldalainak száma szerint csökkenő sorrendbe és a sorbarakott.txt állományba mentsük el.
szortirozni = konyvek
sorbaRendez(szortirozni,"csökkenő")
fajlbaIras(szortirozni,"sorbarakott.txt")