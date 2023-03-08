print("Kérem adja meg hány elemű a számpiramis?")
sor = int(input())    

for i in range(sor, 1, -1):    
    for j in range(i, 0, -1):  
        print(f"{j}", end=' ')  
    print(" ")  
print("1")