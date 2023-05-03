from parts import *

class PC():
    def __init__(self) -> None:
        super().__init__()
        self.alaplap :Alaplap = Alaplap("AMD", "4", 2020, "AM4", "GIGABYTE B450 AORUS Elite V2")
        self.gpu :GPU = GPU("ASUS", 12, 2020, 1882, "NVIDIA GeForce RTX 3060")
        self.cpu :CPU = CPU("AMD", 3.8, 2020, "AM4", "Ryzen 7 5800X")
        self.ram :RAM = RAM("Kingston", 16, 2020, "FURY beast")
        self.tarhely :Tarhely = Tarhely("Kingston", 960, 2020, 450, 500, "SA400S37/960G")
        self.psu :PSU = PSU("ASUS", 850, 2020, "ROG-STRIX-850G")

    def __str__(self) -> str:
        return f"\nA számítógép adatai\n\n\t{self.alaplap}\n\n\t{self.gpu}\n\n\t{self.cpu}\n\n\t{self.ram}\n\n\t{self.tarhely}\n\n\t{self.psu}\n"