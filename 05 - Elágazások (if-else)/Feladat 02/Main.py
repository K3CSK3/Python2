from os import system

number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if (number > 0):
    print(f"A szám {number} pozitív")
else :
    print(f"A szám {number} negatív")