from os import system

number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if (number > 0):
    print(f"A szám {number} nagyobb mint nulla")
else :
    print(f"A szám {number} kisebb mint nulla")