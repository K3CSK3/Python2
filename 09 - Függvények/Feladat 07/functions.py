import random
def randomSzam() -> int:
    tomb = ""
    tomb = str(random.randrange(1,10000))
    for i in range(9):
        randomNum = random.randrange(1,10000)
        tomb += ";" + str(randomNum)
    return tomb

def osszeadas(blokk:str) -> int:
    osszeg = 0
    for i in range(10):
        osszeg += int(blokk.split(";")[i])
    return osszeg

def nagyobb(num1:int, num2:int) -> int:
    if (num1 > num2):
        return num1
    elif (num1 < num2):
        return num2