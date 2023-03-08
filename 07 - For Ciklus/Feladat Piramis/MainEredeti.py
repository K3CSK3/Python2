sor :int = 0
lista :list = [1]

print("Kérem adja meg hány elemű a számpiramis?")
sor = int(input())
for i in range(1, sor+1):
    print('  '.join(map(str, lista)))
    lista.append(f" {i+1} ")