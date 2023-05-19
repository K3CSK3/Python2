class Tanulo():
    def __init__(self, nev: str, atlag: float) -> None:
        super().__init__()
        self.nev: str = nev
        self.atlag: float = atlag

    def __str__(self) -> str:
        return f"Név: {self.nev} \t Átlag: {self.atlag}"