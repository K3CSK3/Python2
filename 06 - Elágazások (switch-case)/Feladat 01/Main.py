from os import system

day :int = None

print("Adja meg a hét egyik napját (szám):",end='')
day = int(input().strip())

system('cls')

match day:
    case 1:
        print("Ez a nap a Hétfő!")
    case 2:
        print("Ez a nap a Kedd!")
    case 3:
        print("Ez a nap a Szerda!")
    case 4:
        print("Ez a nap a Csütörtök!")
    case 5:
        print("Ez a nap a Péntek!")
    case 6:
        print("Ez a nap a Szombat!")
    case 7:
        print("Ez a nap a Vasárnap!")
    case _:
        print("Nincs ilyen nap!")