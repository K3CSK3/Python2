from os import system

name :str = None
pressedKey :str = None


print("Adja meg a nevét: ",end='')
name = input()

print("Üssön le egy billentyűt ",end='')
pressedKey = input()


system('cls')


print(f"{name} ön a/az {pressedKey} billentyűt nyomta meg!")