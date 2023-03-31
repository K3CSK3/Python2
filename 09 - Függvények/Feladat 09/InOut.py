def inOutMoney() -> float:
    num :float = None
    while (num == None):
        bevitel: str = None
        isNumber :bool = False
        bevitelCopy :str = None

        print("Adjon meg a pénz mennyiségét HUF-ban: ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(".", "").replace("-", "")
        isNumber = bevitelCopy.isnumeric()
        if (isNumber):
            num = float(bevitel)
        else:
            print("Nem számot adott meg!\n\n")
    return num

def inOutCurrency() -> str:
    text :str = None
    while (text == None):
        bevitel: str = None
        print("Adja meg milyen pénznembe szeretne konvertálni(CHF, USD, JPY): ",end="")
        bevitel = input()
        bevitelCopy = bevitel.replace(" ", "")

        if (bevitelCopy.isalpha()):
            text = str(bevitel)
        else:
            print("Nem pénznemet adott meg!\n\n")
            
    return text


def kiiras(adat:str) -> None:
    print(adat)