from typing import *
from io import open
import os
from modell.tanulo import *

tanulo: Tanulo = None
osszesTanulo: List[Tanulo] = []
adat: List[str] = []

fajlNeve: str ='.\\data\\adatok.txt'
alapEleres: str = os.path.dirname(os.path.abspath(__file__))
teljesEleres = os.path.join(alapEleres, fajlNeve)

try:
    with open(teljesEleres, encoding="utf-8", mode="r") as file:
        for line in file:
            tanulo = line.strip()
            adat = tanulo.split("\t")
            osszesTanulo.append(tanulo)
            tanulo = Tanulo(adat[0],float(adat[1].replace(",",".")))

except FileNotFoundError as ex:
    print(f"{ex.filename} nem található vagy nem létezik!")

for line in osszesTanulo:
    print(line)