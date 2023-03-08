from os import system

number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

print("A szám:")
if (number%2 == 0):
    print("Páros")
elif (number%2):
    print("Páratlan")

if (number > 0):
    print("Pozitív")
elif (number < 0):
    print("Negatív")
elif (number == 0):
    print("Nulla")

if (number%5 == 0):
    print("Osztható öttel")
elif (number%5):
    print("Nem osztható öttel")