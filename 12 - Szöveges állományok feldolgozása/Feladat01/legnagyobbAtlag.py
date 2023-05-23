from modell.tanulo import Tanulo
def legnagyobbAtlagKereso(tanulok: list[Tanulo]) -> list[Tanulo]:
    legnagyobbAtlag: Tanulo = tanulok[0]

    for index in range(1, len(tanulok), 1):
        
        if tanulok[index].atlag > legnagyobbAtlag.atlag:
            legnagyobbAtlag = tanulok[index]

        # if tanulok[index].atlag == legnagyobbAtlag.atlag:
        #     legnagyobbAtlag.append(tanulok[index])
        
    return legnagyobbAtlag