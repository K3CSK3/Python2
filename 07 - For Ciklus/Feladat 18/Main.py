start :int = None
end :int = None
osszeg :int = 0

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())


for i in range(start, end+1, 2):
    osszeg += i
for i in range(start+1, end+1, 2):
    osszeg += (i*-1)
print(osszeg)