from modell.konyv import *
from typing import *
import os
def konyvBeolvasas(fileNev:str) -> list[Konyvek]:
    
    konyvek: List[Konyvek] = []

    alapEleres: str = os.path.dirname(os.path.abspath(__file__))+"/data/"
    teljesEleres = os.path.join(alapEleres , fileNev)
    
    try:

        with open(teljesEleres, encoding="utf-8", mode="r") as file:

            for line in file:
                adat = line.split("\t")
                konyv = Konyvek()
                konyv.vezeteknev = adat[0]
                konyv.keresztnev = adat[1]
                konyv.születesidatum = datetime.fromisoformat(adat[2])
                konyv.cim = adat[3]
                konyv.isbn = adat[4]
                konyv.kiado = adat[5]
                konyv.kiadvasiev = int(adat[6])
                konyv.ar = float(adat[7])
                konyv.tema = adat[8]
                konyv.oldalszam = int(adat[9])
                konyv.honorarium = float(adat[10])
                konyvek.append(konyv)

        return konyvek
    
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található vagy nem létezik!")

        return []
