from os import system

numberOne :int = None
numberTwo :int = None

print("Adjon meg egy számot: ",end='')
numberOne = int(input())

print("Adjon még egy egy számot: ",end='')
numberTwo = int(input())

system('cls')

if (numberOne > numberTwo):
    print(f"Az első szám {numberOne} nagyobb mint a második {numberTwo}")
elif (numberOne < numberTwo):
    print(f"A második szám {numberTwo} kisebb mint az első {numberOne}")