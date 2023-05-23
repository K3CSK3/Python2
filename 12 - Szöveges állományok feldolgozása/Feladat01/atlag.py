from modell.tanulo import Tanulo

def atlagSzamito(tanulok: list[Tanulo]) -> float:
    osszes = 0
    
    for line in tanulok:
        osszes += line.atlag

    atlag = osszes/len(tanulok)

    return round(atlag,2)