print("Kérem adja meg hány elemű a számpiramis?")
sor = int(input())

oszlop = (2 * sor) - 2  
for i in range(0, sor+1):  
    for j in range(0, oszlop):  
        print(end="  ")  
    oszlop -= 1
    for j in range(1, i*2):  
        print(f" {j}", end='')  
    print(" ")