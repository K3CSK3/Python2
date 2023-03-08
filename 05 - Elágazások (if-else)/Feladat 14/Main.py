from os import system

numberOne :int = None
numberTwo :int = None
numberThree :int = None

print("Adjon meg egy számot: ",end='')
numberOne = int(input())

print("Adjon még egy számot: ",end='')
numberTwo = int(input())

print("Adjon egy harmadik számot: ",end='')
numberThree = int(input())

system('cls')

if ((numberOne % numberTwo) == 0 and (numberOne % numberThree) == 0):
    print("Az első szám osztható mind két számmal")

elif ((numberOne % numberTwo) == 0 and numberOne % numberThree):
    print("Az első szám csak a második számmal osztható")

elif (numberOne % numberTwo and (numberOne % numberThree) == 0):
    print("Az első szám csak a harmadik számmal osztható")
else :
    print("Osztható hattal és néggyel")