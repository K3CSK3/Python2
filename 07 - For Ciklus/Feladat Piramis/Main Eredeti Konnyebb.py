print("Kérem adja meg hány elemű a számpiramis?")
szam = int(input()) 
for i in range(0, szam+1): 
    for j in range(1, i+1):
        print(f"{j} ", end="") 
    print() 