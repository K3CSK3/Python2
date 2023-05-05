class GPU():
    def __init__(self, gyarto: str, memoria: int, kiadaseve: int, orajel: int, model: str) -> None:
        super().__init__()
        self.gyarto: str = gyarto
        self.memoria: int = memoria
        self.kiadaseve: int = kiadaseve
        self.orajel: int = orajel
        self.model: str = model

    def __str__(self) -> str:
        return f"A VIDEÓKÁRTYA adatai:\n\t\tGyártja: {self.gyarto}\n\t\tModell: {self.model}\n\t\tMemóriája: {self.memoria}\n\t\tKiadásának éve: {self.kiadaseve}\n\t\tÓrajele: {self.orajel}"