start :int = None
end :int = None
osszeg :int = 0

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())


if (start % 3 == 1):
    start += 2
elif (start % 3 == 2):
    start += 1

for i in range(end, start-1, -3):
    osszeg += 1
print(f"{osszeg} szám osztható 3-al")