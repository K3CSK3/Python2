from os import system

numberOfPeople :int = None

groupDiscount :float = None
schoolDiscount :float = None
studentDiscount :float = None

price :int = None
fullPrice :int = None
destination :int = None

bestOffer :str = None

print("1-Velencei tó(6000Ft/fő)\n2-Tihany és Balatonfüred(7500Ft)\nVálassza ki a kirándulás helyszínét: ",end='')
destination = int(input())
if destination == 1:
    price = 6000
elif destination == 2:
    price = 7500
else:
    print("Ilyen szállás jelenleg nincs!")

print("Kérem a létszámot: ",end='')
numberOfPeople = int(input())

fullPrice = price * numberOfPeople

# Csoportos kedvezmény kiszámolása Ft/fő
if (numberOfPeople < 5):
    groupDiscount = price * 1
elif (numberOfPeople >= 5 and numberOfPeople <= 15):
    groupDiscount = price * 0.95
elif (numberOfPeople >= 16 and numberOfPeople <= 25):
    groupDiscount = price * 0.92
elif (numberOfPeople > 25):
    groupDiscount = price * 0.85

# Intézményi kedvezmény kiszámolása Ft/fő
if (numberOfPeople < 5):
    schoolDiscount = price
elif (numberOfPeople >= 5 and numberOfPeople <= 10):
    schoolDiscount = (fullPrice - (price))/numberOfPeople
elif (numberOfPeople >= 11 and numberOfPeople <= 20):
    schoolDiscount = (fullPrice - (price * 2))/numberOfPeople
elif (numberOfPeople >= 21):
    schoolDiscount = (fullPrice - (price * 3))/numberOfPeople

# Diák kedvezmény Ft/fő
studentDiscount = price * 0.92

system('cls')

print(f"Csoportkedvezményes ár: {round(groupDiscount,0)} Ft/fő")
print(f"Intézmény kedvezményes ár: {round(schoolDiscount,0)} Ft/fő")
print(f"Diák kedvezményes ár: {round(studentDiscount,0)} Ft/fő")

#Legjobb ajánlat megállapítása
if ((groupDiscount < schoolDiscount) and (groupDiscount < studentDiscount)):
    bestOffer = (f"A legjobb ajánlat a Csoportkedvezmény! {numberOfPeople} fő esetén: {round(groupDiscount,0)} Ft/fő")
elif ((schoolDiscount < groupDiscount) and (schoolDiscount < studentDiscount)):
    bestOffer = (f"A legjobb ajánlat az Intézményi kedvezmény! {numberOfPeople} fő esetén: {round(schoolDiscount,0)} Ft/fő")
elif ((studentDiscount < groupDiscount) and (studentDiscount < schoolDiscount)):
    bestOffer = (f"A legjobb ajánlat a Diák kedvezmény! {numberOfPeople} fő esetén: {round(studentDiscount,0)} Ft/fő")
print(f"-------------------------------------------------------------\n{bestOffer}")