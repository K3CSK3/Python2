def osszeadas(szam1:float, szam2:float) -> float:
    osszeg :float = None
    osszeg = szam1 + szam2 
    return osszeg

def kivonas(szam1:float, szam2:float) -> float:
    kulonbseg :float = None
    kulonbseg = szam1 - szam2 
    return kulonbseg

def szorzas(szam1:float, szam2:float) -> float:
    szorzat :float = None
    szorzat = szam1 * szam2 
    return szorzat

def osztas(szam1:float, szam2:float) -> float:
    hanyados :float = None
    hanyados = szam1 / szam2 
    return hanyados

def printToCons(szam1:float, szam2:float, result:float, function:str,) -> None:
    print(f"{szam1} {function} {szam2} = {result}")