from os import system

numberOne :int = None
numberTwo :int = None
eredmeny :float = None


print("Adja meg az első számot: ",end='')
numberOne = int(input())

print("Adja meg a második számot: ",end='')
numberTwo = int(input())

eredmeny = numberOne + numberTwo


system('cls')

print(f"A számok eredménye {eredmeny}.")
