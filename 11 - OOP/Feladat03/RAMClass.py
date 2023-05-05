class RAM():
    def __init__(self, gyarto: str, meret: int, kiadaseve: int, model: str) -> None:
        super().__init__()
        self.gyarto: str = gyarto
        self.meret: int = meret
        self.kiadaseve: int = kiadaseve
        self.model: str = model

    def __str__(self) -> str:
        return f"A MEMÓRIA adatai:\n\t\tGyártja: {self.gyarto}\n\t\tModell: {self.model}\n\t\tMérete: {self.meret} GB\n\t\tKiadásának éve: {self.kiadaseve}"