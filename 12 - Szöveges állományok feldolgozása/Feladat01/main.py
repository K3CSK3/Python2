from typing import *
from tanuloIO import *
from modell.tanulo import *
from atlag import *
from legnagyobbAtlag import *

tanulok :List[Tanulo] = tanuloBekeres()

print("OSztály Tanulói")
for line in tanulok:
    print(line)

osztalyLetszam: int = len(tanulok)
print(f"\n\nAz osztályban {osztalyLetszam} tanuló jár\n\n")

osztalyAtlag = atlagSzamito(tanulok)
print(f"az osztaly atlag {osztalyAtlag}")

legnagyobbAtlag = legnagyobbAtlagKereso(tanulok)
print(f"Az osztályban a legnagyobb átlag:\n{legnagyobbAtlag}")