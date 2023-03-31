def konvertalo(penz:float,varando:str) ->float:
    CHF :float = 0.55
    USD :float = 0.8
    JPY :float = 0.75

    EUR = penz*0.0026

    if varando == "CHF":
        konvErtek = penz*CHF
    elif varando == "USD":
        konvErtek = penz*USD
    elif varando == "JPY":
        konvErtek = penz*JPY

    vissza = str(EUR)+ "Euró, " + str(konvErtek) + varando

    return vissza