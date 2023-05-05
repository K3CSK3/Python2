class PSU():
    def __init__(self, gyarto: str,  aramfelvetel: int,  kiadaseve: int,  model: str) -> None:
        super().__init__()
        self.gyarto: str = gyarto
        self.aramfelvetel: int = aramfelvetel
        self.kiadaseve: int = kiadaseve
        self.model: str = model

    def __str__(self) -> str:
        return f"A TÁPEGYSÉG adatai:\n\t\tGyártja: {self.gyarto}\n\t\tModell: {self.model}\n\t\tÁramfelvétele {self.aramfelvetel}\n\t\tKiadásának éve: {self.kiadaseve}"