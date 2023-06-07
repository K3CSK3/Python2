class Jatekos():
    def __init__(self) -> None:
        super().__init__()
        self.nev: str = None
        self.magassag: int = None
        self.poszt: str = None
        self.nemzetiseg: str = None
        self.csapat: str = None
        self.orszag: str = None

    def __str__(self) -> str:
        return f"{self.nev} magassága: {self.magassag}, {self.poszt} posztban játszik, {self.orszag} {self.nemzetiseg} nemzetiségű {self.csapat} csapatban"