def konverter(tipus:str, mennyiseg:float) -> float:
    if tipus == "K":
        konvertalt = mennyiseg + 273.15
    elif tipus == "F":
        konvertalt = 9/5*mennyiseg+32
    return konvertalt
