from os import system

numberOne :int = None
numberTwo :int = None
numberThree :int = None
eredmeny :float = None


print("Adja meg az első számot: ",end='')
numberOne = int(input())

print("Adja meg a második számot: ",end='')
numberTwo = int(input())

print("Adja meg a harmadik számot: ",end='')
numberThree = int(input())

eredmeny = (numberOne - numberTwo) * numberThree


system('cls')

print(f"Az első két szám különbözetének és a harmadik szám szorzata: {eredmeny}")