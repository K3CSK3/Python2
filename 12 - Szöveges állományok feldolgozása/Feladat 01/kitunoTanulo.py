from modell.tanulo import Tanulo
def kitunoTanulo(tanulok: list[Tanulo]) -> bool:
    for tanulo in tanulok:
        if tanulo.atlag == 5.00:
            return True
    return False