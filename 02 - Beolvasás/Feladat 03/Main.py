from os import system

name : str = None
height : int = None


print("Adja meg a nevét ",end='')
name = str(input())

print("Adja meg a magasságát(m) ",end='')
height = float(input())


system('cls')


print(f"{name} az ön magassága {height}m!\n")