from motor import Motor
from typing import *
def adatMennyisegKereso(motorok: List[Motor]) -> int:
    adatHossz = len(motorok)
    return adatHossz

def evUtanGyartottak(motorok: List[Motor], gyartasiEv) -> int:
    darab: int = 0
    for motor in motorok:
        if (int(motor.gyartasiEv) >= gyartasiEv):
            darab += 1
    return darab

def arAtlag(motorok: List[Motor]) -> float:
    osszesAr = 0
    for motor in motorok:
        osszesAr += int(motor.ar)
    atlag = osszesAr/len(motorok)
    return atlag

def legidosebbMotor(motorok :List[Motor]) -> List[Motor]:
    legidosebbEve = 10000
    for motor in motorok:
        if motor.gyartasiEv < legidosebbEve:
            legidosebbEve = motor.gyartasiEv
            legidosebb = motor
    return legidosebb

def sorbaRakas(motorok: List[Motor]) -> None:
    ideig = None
    for i in range(len(motorok)):
        for j in range(len(motorok)):
            if motorok[j].ar > motorok[i].ar:
                ideig = motorok[j]
                motorok[j] = motorok[i]
                motorok[i] = ideig