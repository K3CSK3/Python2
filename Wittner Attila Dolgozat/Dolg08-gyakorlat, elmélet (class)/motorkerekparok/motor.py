#Készítsen olyan adatszerkezetet, amely képes eltárolni egy konkrét motorkerékpárt (az adatok.txt állomány egy sorában leírt motorkerékpárt). (1)
class Motor():
    def __init__(self) -> None:
        super().__init__()
        self.gyarto: str = None
        self.modell: str = None
        self.gyartasiEv: int = 0
        self.ar: int = 0

    def __str__(self) -> str:
        return f"{self.gyarto} átlat gyártott {self.modell}({self.gyartasiEv}) modell ára {self.ar}EUR\n"