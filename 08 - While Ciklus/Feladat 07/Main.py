elsoErtek :int = None
masodikErtek :int = 0
bevitel :str = None


while (elsoErtek == None):
    print("Adjon meg egy számot: ",end="")
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        elsoErtek = int(bevitel)
    else:
        print("Nem számot adott meg!")

while (masodikErtek == None or elsoErtek > masodikErtek):
    print("Adjon meg egy nagyobb számot számot: ",end="")
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        masodikErtek = int(bevitel)
    else:
        print("Nem számot adott meg!")


for i in range(masodikErtek, elsoErtek, -1):
    print(i)