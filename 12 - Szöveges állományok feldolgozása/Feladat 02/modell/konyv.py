from datetime import *
class Konyvek():
    def __init__(self,) -> None:
        super().__init__()
        self.vezeteknev: str = None
        self.keresztnev: str = None
        self.születesidatum: datetime.date = None
        self.cim: str = None
        self.isbn: int = None
        self.kiado: str = None
        self.kiadvasiev: int = None
        self.ar: float = None
        self.tema: str = None
        self.oldalszam: int = None
        self.honorarium: int = None
    def __str__(self) -> str:
        return f"{self.cim}({self.isbn}) írta {self.vezeteknev} {self.keresztnev} (született: {self.születesidatum}) kiadva {self.kiadvasiev} {self.kiado} által. Ára: {self.ar} Ft, témája: {self.tema}, oldalainak száma: {self.oldalszam}\n"