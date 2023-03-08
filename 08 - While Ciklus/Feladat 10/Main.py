szam :int = 100
maradek :int = 0
valtozottSzam :int = 0
darab :int = 0
ottel :int = 0
hetteldb :int = 0
bevitel :str = None

while (szam > 99 or szam < 0):
    print("Adjon meg egy számot (maximum 2 jegyűt): ", end="")
    bevitel = input()
    bevitelCopy = bevitel.replace(".", "").replace("-", "")
    isNumber = bevitelCopy.isnumeric()
    if (isNumber):
        szam = int(bevitel)
    else:
        print("Nem számot adott meg")

print(f"0 és {szam} közti páros számok: ",end='')
for i in range(0, szam, 2):
    print(f", {i}",end='')

maradek = szam % 5
valtozottSzam = szam - maradek

for i in range(0, valtozottSzam+1, 5):
    ottel += i

print(f"\n5-el osztható számok összege: {ottel}")

maradek = szam % 11
valtozottSzam = szam - maradek

for i in range(0, valtozottSzam+1, 11):
    darab =+ 1
print(f"0 és {szam} között 11-el osztható számok összege: {darab}")

maradek = szam % 7
valtozottSzam = szam - maradek + 3
for i in range(0,valtozottSzam+1, 7):
    hetteldb += 1

print(f"0 és {szam} közötti számok melyek 3-at adnak maradékba ha 7-el oszjuk el: {hetteldb}")