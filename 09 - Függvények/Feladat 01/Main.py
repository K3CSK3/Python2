from functions import *
from InOut import InOut as consoleInput


szam1 :float = None
szam2 :float = None
osszeg :float = None

szam1 = consoleInput()
szam2 = consoleInput()

osszeg =  osszeadas(szam1, szam2)
printToCons(szam1, szam2,  osszeg, "+")

osszeg =  osszeadas(szam1, szam2)
printToCons(szam1, szam2,  osszeg, "-")

osszeg =  osszeadas(szam1, szam2)
printToCons(szam1, szam2,  osszeg, "*")

osszeg =  osszeadas(szam1, szam2)
printToCons(szam1, szam2,  osszeg, "/")