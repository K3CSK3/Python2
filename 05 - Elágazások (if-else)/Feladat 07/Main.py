from os import system

number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if (number % 5):
    print("Nem osztható öttel(maradék nélkül)")
else:
    print("A szám osztható 5-el")