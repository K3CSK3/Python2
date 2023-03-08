from os import system

numberOne :int = None
numberTwo :int = None

print("Adjon meg egy számot: ",end='')
numberOne = int(input())

print("Adjon még egy egy számot: ",end='')
numberTwo = int(input())

system('cls')

if (numberOne % numberTwo):
    print("Az első számnak nem osztója a második")
else:
    print("Az első számnak osztója a második")