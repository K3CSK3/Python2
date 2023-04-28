def nev_bekeres() -> str:
    name = None
    while (name == None or len(name) <= 3):
        print("Adja meg a nevét: ",end="")
        nameInput = input().strip()
        nameCopy = nameInput.isalpha()
        if (nameCopy):
            name = nameInput
        else:
            print("Nem nevet adott meg")
    return name

def oraszam_bekeres() -> int:
    ora = None #tipus
    while (ora == None):
        print("Adja meg a ledolgozott órák számát: ",end="")
        oraInput = input() #tipus
        if (oraInput.isnumeric() and int(oraInput) >= 0):
            ora = int(oraInput)
        else:
            print("Nem óraszámot adott meg vagy negatív értéket adott meg")
    return ora

def tulora_bekeres() -> int: #miert int?
    tulOra = None #tipus
    while (tulOra == None):
        print("Adja meg a túlórák számát: ",end="")
        tulOraInput = input() #tipus
        if (tulOraInput.isnumeric() and int(tulOraInput) >= 0):
            tulOra = int(tulOraInput)
        else:
            print("Nem óraszámot adott meg vagy negatív értéket adott meg")
    return tulOra

def kiiras(munkasnev:str, penz:int, nap:str) -> None: #pent miert int?
    print(f"Hétfő {munkasnev} tárgyhavi fizetése {penz} HUF" )