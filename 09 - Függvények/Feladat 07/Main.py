from functions import *
from InOut import *

tombEgy = randomSzam()
tombKetto = randomSzam()


osszeg1 = osszeadas(tombEgy)
osszeg2 = osszeadas(tombKetto)

nagyobbErtek = nagyobb(osszeg1, osszeg2)

egybeKiiras(tombEgy)
egybeKiiras(tombKetto)

kiiras(nagyobbErtek, osszeg1, osszeg2)