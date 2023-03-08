from os import system

numberOne :float = None
numberTwo :float = None
numberThree :float = None
eredmeny :float = None

print("Adja meg az elsó számot: ",end='')
numberOne = float(input())

numberOne += 0.5

print("Adja meg a második számot: ",end='')
numberTwo = float(input())

numberTwo -= 0.7

print("Adja meg a harmadik számot: ",end='')
numberThree = float(input())

eredmeny = (numberOne * numberTwo) % numberThree

system('cls')

print(f"Az első két szám szoratának és harmadik szám hányadosának maradéka: {eredmeny}")