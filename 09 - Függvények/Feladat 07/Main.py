from functions import *
from InOut import *

tombEgy = randomSzam()
tombKetto = randomSzam()

print(tombEgy, tombKetto)

osszeg1 = osszeadas(tombEgy)
osszeg2 = osszeadas(tombKetto)

nagyobbErtek = nagyobb(osszeg1, osszeg2)

kiiras(nagyobbErtek, osszeg1, osszeg2)