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


class RAM():
    def __init__(self, gyarto: str, meret: int, kiadaseve: int, model: str) -> None:
        super().__init__()
        self.gyarto: str = gyarto
        self.meret: int = meret
        self.kiadaseve: int = kiadaseve
        self.model: str = model

    def __str__(self) -> str:
        return f"A MEMÓRIA adatai:\n\t\tGyártja: {self.gyarto}\n\t\tModell: {self.model}\n\t\tMérete: {self.meret} GB\n\t\tKiadásának éve: {self.kiadaseve}"


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


class PSU():
    def __init__(self, gyarto: str,  aramfelvetel: int,  kiadaseve: int,  model: str) -> None:
        super().__init__()
        self.gyarto: str = gyarto
        self.aramfelvetel: int = aramfelvetel
        self.kiadaseve: int = kiadaseve
        self.model: str = model

    def __str__(self) -> str:
        return f"A TÁPEGYSÉG adatai:\n\t\tGyártja: {self.gyarto}\n\t\tModell: {self.model}\n\t\tÁramfelvétele {self.aramfelvetel}\n\t\tKiadásának éve: {self.kiadaseve}"


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
