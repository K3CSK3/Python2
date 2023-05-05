from Szamitogep import PC

from AlaplapClass import Alaplap
from GPUClass import GPU
from CPUClass import CPU
from RAMClass import RAM
from TarhelyClass import Tarhely
from PSUClass import PSU

alaplap: Alaplap = Alaplap("AMD", "4", 2020, "AM4", "GIGABYTE B450 AORUS Elite V2")
videoKartya: GPU = GPU("ASUS", 12, 2021, 1882, "NVIDIA GeForce RTX 3060")
processzor: CPU = CPU("AMD", 3.8, 2020, "AM4", "Ryzen 7 5800X")
memoria: RAM = RAM("Kingston", 16, 2021, "FURY beast")
tarhely: Tarhely = Tarhely("Kingston", 960, 2018, 450, 500, "SA400S37/960G")
tapegyseg: PSU = PSU("ASUS", 850, 2020, "ROG-STRIX-850G")

szamitogep :PC = PC(alaplap,videoKartya,processzor,memoria,tarhely,tapegyseg)

print(szamitogep)