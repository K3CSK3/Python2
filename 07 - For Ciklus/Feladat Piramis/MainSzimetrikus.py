sor :int = 0
lista :list = []

print("Kérem adja meg hány elemű a számpiramis?")
sor = int(input())

for i in range(1, sor*2, 1):
    lista.append("")
lista.append(1)

for i in range(1, sor*2, 2):
    print(' '.join(map(str, lista)))
    del lista[0]
    del lista[0]
    lista.append(f"{i+1}")
    lista.append(f"{i+2}")