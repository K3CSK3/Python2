from os import system

bandName :str  = None
songName :str  = None
songLength :float = None


print("Írja be a kedvenc bandájának nevét: ",end='')
bandName = str(input())

print(f"Írja be a legjobb zeneszámát {bandName} bandának: ",end='')
songName = str(input())

print("Írja be ennek a zeneszámnak a hosszát: ",end='')
songLength = float(input())


system('cls')


print(f"Az ön kedvenc együttesének {bandName} a legjobb zeneszáma {songName} melynek hossza {songLength} perc !",end='')