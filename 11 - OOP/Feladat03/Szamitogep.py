from AlaplapClass import Alaplap
from GPUClass import GPU
from CPUClass import CPU
from RAMClass import RAM
from TarhelyClass import Tarhely
from PSUClass import PSU

class PC():
    def __init__(self,alaplap :Alaplap, videoKartya :GPU, processzor :CPU, memoria :RAM, tarhely :Tarhely, tapegyseg :PSU) -> None:
        super().__init__()
        self.alaplap :Alaplap = alaplap
        self.gpu :GPU = videoKartya
        self.cpu :CPU = processzor
        self.ram :RAM = memoria
        self.tarhely :Tarhely = tarhely
        self.psu :PSU = tapegyseg

    def __str__(self) -> str:
        return f"\nA számítógép adatai\n\n\t{self.alaplap}\n\n\t{self.gpu}\n\n\t{self.cpu}\n\n\t{self.ram}\n\n\t{self.tarhely}\n\n\t{self.psu}\n"