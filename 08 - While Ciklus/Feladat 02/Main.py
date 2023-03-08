nev :str = "a"

while (len(nev) <= 1):
    print("Adja meg a nevet: ",end ="")
    nev = input().strip()
print(f"Üdvözlöm {nev}!")