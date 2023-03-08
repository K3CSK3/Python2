from os import system


brand :str = None
model :str = None
type :str = None
cubic :int = None
year :int = None


print("Adja meg a márkát: ",end='')
brand = str(input())

print("Adja meg a modellt: ",end='')
model = str(input())

print("Adja meg a típust: ",end='')
type = str(input())

print("Adja meg a motor köbcentijét: ",end='')
cubic = int(input())

print("Adja meg a megjelenési évet: ",end='')
year = int(input())


system('cls')


print(f"Márka : {brand}\nModell : {model}\nTípus : {type}\nKöbcenti : {cubic}\nMegjelenési év : {year}")