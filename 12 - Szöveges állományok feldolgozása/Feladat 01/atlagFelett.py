from modell.tanulo import Tanulo
def atlagFelettiTanulok(tanulok: list[Tanulo], osztalyAtlag: float) -> list[Tanulo]:
    atlagFelett = []
    
    for tanulo in tanulok:
        if(tanulo.atlag >= osztalyAtlag):
            atlagFelett.append(tanulo)

    return atlagFelett