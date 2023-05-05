class Alaplap():
    def __init__(self, gyarto: str, RAMslot: str, kiadaseve: int, CPUaljzat: str, model: str) -> None:
        super().__init__()
        self.gyarto: str = gyarto
        self.RAMslot: str = RAMslot
        self.kiadaseve: int = kiadaseve
        self.CPUaljzat: str = CPUaljzat
        self.model: str = model

    def __str__(self) -> str:
        return f"Az ALAPLAP adatai:\n\t\tGyártja: {self.gyarto}\n\t\tModell: {self.model}\n\t\tRAMszlottok: {self.RAMslot}\n\t\tKiadásának éve: {self.kiadaseve}\n\t\tProcesszor foglalat: {self.CPUaljzat}"