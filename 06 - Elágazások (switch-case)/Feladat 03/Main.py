from os import system

drink :int = None

print("Adja meg a kívánt italt(1-4)",end='')
drink = int(input().strip())

system('cls')

match drink:
    case 1:
        print("Coca Cola")
    case 2:
        print("Pepsi")
    case 3:
        print("Fanta")
    case 4:
        print("Sprite")
    case _:
        print("Az autómata nem tud ilyen italt felszolgálni")