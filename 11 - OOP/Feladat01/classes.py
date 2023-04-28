from math import pow

class Negyzet:
    def __init__(self,a:float=0) -> None:
        super().__init__()
        self.oldal :float = a
    
    def terulet(self)->float:
        return pow(self.oldal,2)

    def kerulet(self)->float:
        return self.oldal * 4
    
    def terfogat(self)->float:
        return pow(self.oldal,3)
