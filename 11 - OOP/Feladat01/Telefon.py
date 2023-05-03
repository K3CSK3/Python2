class Telefon:
    def __init__(self,marka:str,tipus:str,megjel:int,akkumulator:int,tarhely:int,memoria:int,kijelzo:int) -> None:
        super().__init__()
        self.marka = marka
        self.tipus = tipus
        self.megjelenes = megjel
        self.mAh = akkumulator
        self.tarhely = tarhely
        self.memoria = memoria
        self.kijelzoMeret = kijelzo

    def kiiras(self) -> None:
        print(f"\nTelefon Adatai:\n\tMárkája:{self.marka}\n\tTípusa:{self.tipus}\n\tMegjelenési Dátuma:{self.megjelenes}\n\tAkkumulátor kapacitása:{self.mAh}mAh\n\tHozzáférhető Tárhely:{self.tarhely} GB\n\tMemória:{self.memoria} GB\n\tKijelző Átmérője:{self.kijelzoMeret} in\n")
