from os import system

name :str = None
yearOfBirth :int = None


print("Adja meg a nevét: ",end='')
name = input()

print("Adja meg a születési évét: ",end='')
yearOfBirth = int(input())


system('cls')


print(f"{name} ön {yearOfBirth} született!\n")