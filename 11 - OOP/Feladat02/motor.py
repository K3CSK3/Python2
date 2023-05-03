class motor():
    def __init__(self) -> None:
        super().__init__()
        self.tipus :str = None
        self.gyarto :str = None
        self.modell :str = None
        self.loero :int = 0
        self.henger :int = 0
        self.gyartasiev :int = 0
        self.nyomatek :int = 0
        self.fogyasztas :int = 0
    def __str__(self) -> str:
        return f"\nA motorkerépkár adatai:\n\tTípusa: {self.tipus}\n\tGyártja: {self.gyarto}\n\tModell: {self.modell}\n\tLóereje: {self.loero} HP\n\tHenegerek: {self.henger}\n\tGyártási év: {self.gyartasiev}\n\tNyomatéka: {self.nyomatek}\n\tFogyasztása: {self.fogyasztas} l/100km\n"