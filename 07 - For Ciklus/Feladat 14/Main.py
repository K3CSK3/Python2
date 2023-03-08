start :int = None
end :int = None
osszeg :int = 0
osszeg2 :int = 1

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())


for i in range(end, start-1, -1):
    if (i % 5 == 0):
        osszeg += i
    elif (i % 7 == 0):
        osszeg2 += i
if osszeg > osszeg2:
    print(f"Az öttel osztható számok összege a nagyobb")
else:
    print(f"A héttel osztható számok összege a nagyobb")