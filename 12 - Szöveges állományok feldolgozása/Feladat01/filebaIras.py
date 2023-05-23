import os
from io import *
from typing import *
from modell.tanulo import Tanulo

def kiirasFileba(tanulok :list[Tanulo], fileNev: str) -> None:
    alapUt = os.path.dirname(os.path.abspath(__file__))
    teljesUt = os.path.join(alapUt, fileNev)

    try:
        with open(teljesUt, encoding='utf-8', mode="w") as file :
            for tanulo in tanulok:
                file.write(f"{tanulo.nev}: {tanulo.atlag}\n")
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található")