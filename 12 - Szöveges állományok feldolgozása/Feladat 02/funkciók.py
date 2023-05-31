from modell.konyv import Konyvek
import os

def temaKereses(konyvek: list[Konyvek], tema: str) -> list[Konyvek]:
    infoKonyvek: list[Konyvek] = []
    for konyv in konyvek:
        if(konyv.tema == tema):
            infoKonyvek.append(konyv)
    return infoKonyvek

def evjaratSzamitas(konyvek:list[Konyvek], eleje: int, vege: int) -> list[Konyvek]:
    megfeleloEvjarat:list[Konyvek]=[]
    for konyv in konyvek:
        if(konyv.kiadvasiev >= eleje and konyv.kiadvasiev < vege):
            megfeleloEvjarat.append(konyv)
    return megfeleloEvjarat


def fajlbaIras(konyvek:list[Konyvek], fajlNev:str) -> None:
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    alaput += "/output/"
    teljesUt:str=os.path.join(alaput,fajlNev)
    try:
        with open(teljesUt,encoding="utf-8",mode="w",) as file:
            for konyv in konyvek:
                file.write(f"{konyv}\n")
        
    except FileNotFoundError as ex:
        print(f"{ex.filename} fájl nem található")