from os import system

numberOne :int = None
numberTwo :int = None
numberThree :int = None
numberFour :int = None
eredmeny :float = None


print("Adja meg az első számot: ",end='')
numberOne = int(input())

print("Adja meg a második számot: ",end='')
numberTwo = int(input())

print("Adja meg a harmadik számot: ",end='')
numberThree = int(input())

print("Adja meg a negyedik számot: ",end='')
numberFour = int(input())

eredmeny = (numberOne + numberTwo) / (numberThree - numberFour)

system('cls')

print(f"Az első két szám összegének és a harmadik negyedik szám összegének hányadosa: {eredmeny}")