from os import system

releaseDate :int = None
directorName :str = None
movieName :str = None
mainCharacterName :str = None


print("Adja meg a film kiadási évét: ",end='')
releaseDate = int(input())

print("Adja meg a film rendező nevét: ",end='')
directorName = str(input())

print("Adja meg a filme nevét: ",end='')
movieName = str(input())

print("Adja meg a főszerelplő nevét: ",end='')
mainCharacterName = str(input())


system('cls')


print(f"{releaseDate}-ban {directorName} rendezésében megjelent a/az {movieName} című film {mainCharacterName} főszereplésével!")