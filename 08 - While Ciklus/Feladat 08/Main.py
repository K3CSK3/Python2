udito :str = None
uditoSzam :int = 0
bevitel :str = None


while (uditoSzam < 1 or uditoSzam > 12):
    print("Válasszon egy italt: \n 1 - Fanta \n 2 - Coca Cola \n 3 - Pespsi \n 4 - 7up \n 5 - Sprite \n 6 - Cancada Dry \n 7 - Mountain Dew \n 8 - Red Bull \n 9 - Hell \n 10 - Monster \n 11 - Dr Pepper \n 12 - Schwepppes \n Választás: ",end="")
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        uditoSzam = int(bevitel)
        if (uditoSzam < 0 or uditoSzam > 12):
            print("Nincs ilyen választás") 
    else:
        print("Nem számot adott meg!\n\n")

match uditoSzam:
    case 1: udito = "Fanta"
    case 2: udito = "Coca Cola"
    case 3: udito = "Pepsi"
    case 4: udito = "7up"
    case 5: udito = "Sprite"
    case 6: udito = "Canada Dry"
    case 7: udito = "Mountain Dew"
    case 8: udito = "Red Bull"
    case 9: udito = "Hell"
    case 10: udito = "Monster"
    case 11: udito = "Dr Pepper"
    case 12: udito = "Schweppes"
    case _: udito = "Semmilyen"

print(f"Az ön választása : {udito}")    