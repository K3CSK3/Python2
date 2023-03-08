start :int = None
end :int = None
osszeg :int = 0
osszeg2 :int = 1

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())


for i in range(start, end-1, -1):
    if (i % 2 == 0):
        osszeg += i
    else:
        osszeg2 = osszeg2 * i
print(f" Az Összegük: {osszeg}\n A szorzatuk: {osszeg2}")