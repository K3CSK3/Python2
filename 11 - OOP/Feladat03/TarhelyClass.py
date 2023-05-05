class Tarhely():
    def __init__(self, gyarto: str, meret: int, kiadaseve: int, irassebesseg: int, olvasassebesseg: int, model: str) -> None:
        super().__init__()
        self.gyarto: str = gyarto
        self.meret: int = meret
        self.kiadaseve: int = kiadaseve
        self.irassebesseg: int = irassebesseg
        self.olvasassebesseg: int = olvasassebesseg
        self.model: str = model

    def __str__(self) -> str:
        return f"A TÁRHÉLY adatai:\n\t\tGyártja: {self.gyarto}\n\t\tModell: {self.model}\n\t\tMérete: {self.meret}\n\t\tKiadásának éve: {self.kiadaseve}\n\t\tÍrási sebesség: {self.irassebesseg}\n\t\tÍrási sebesség: {self.olvasassebesseg}"
