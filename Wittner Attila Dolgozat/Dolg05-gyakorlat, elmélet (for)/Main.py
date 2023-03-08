kezdo :int = 0
vegso :int = 0
osszeg :int = 0
darab :int = 0
atlag :int = 0
oszthatoHarommal :int = 0

print("Adja meg a kezdő értéket: ", end='')
kezdo = int(input())

print("Adja meg a végső értéket: ", end='')
vegso = int(input())

for i in range(kezdo, vegso+1, 1):
    osszeg += i
    darab += 1
atlag = osszeg / darab

if kezdo == 1:
    kezdo += 2
elif kezdo == 2:
    kezdo += 1

print(f"A {kezdo} és a {vegso} közti számok összege: {osszeg}.")
print(f"A {kezdo} és a {vegso} közti számok átlaga: {atlag}.")
print(f"A {kezdo} és a {vegso} közti hárommal osztható számok:")
for i in range(kezdo, vegso+1, 3):
    print(f"{i}, ", end='')