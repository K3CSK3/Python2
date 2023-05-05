class CPU():
    def __init__(self, gyarto: str, orajel: int, kiadaseve: int, CPUaljzat: str, model: str) -> None:
        super().__init__()
        self.gyarto: str = gyarto
        self.orajel: int = orajel
        self.kiadaseve: int = kiadaseve
        self.CPUaljzat: str = CPUaljzat
        self.model: str = model

    def __str__(self) -> str:
        return f"A PROCESSZOR adatai:\n\t\tGyártja: {self.gyarto}\n\t\tModell: {self.model}\n\t\tÓrajele: {self.orajel}\n\t\tKiadásának éve: {self.kiadaseve}\n\t\tFoglalat Típusa: {self.CPUaljzat}"