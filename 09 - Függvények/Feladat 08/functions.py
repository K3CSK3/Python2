from math import *
def tavolsagSzamolas(koord1:str, koord2:str) -> float:
    tavolsag :float = 0
    x1 = float(koord1.split(";")[0])
    y1 = float(koord1.split(";")[1])
    x2 = float(koord2.split(";")[0])
    y2 = float(koord2.split(";")[1])
    tavolsag = sqrt((x1-x2)**2 + (y1-y2)**2)
    return tavolsag