sor :int = 0
lista :list = []

print("Kérem adja meg hány elemű a számpiramis?")
sor = int(input())
for i in range(sor+1, 1, -1):
    lista.append(f" {i-1} ")

for i in range(sor, 0, -1):
    print(' '.join(map(str, lista)))
    del lista[0]