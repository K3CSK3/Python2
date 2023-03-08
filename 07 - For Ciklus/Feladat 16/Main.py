start :int = 0
end :int = 0
osszeg1 :int = 0
osszeg2 :int = 0
mennyiseg1 :int = 1
mennyiseg2 :int = 1
print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())


for i in range(start, end-1, -1):
    if (i % 2 == 0):
        osszeg1 += i
        mennyiseg1 += 1
    else:
        osszeg2 += i
        mennyiseg2 += 1
print(f"Páros zsámok átlaga: {osszeg1/mennyiseg1}")
print(f"Páratlan számok összege: {osszeg2/mennyiseg2}")