from os import system

eloetel :int = None
eloetelszoveg :str = None
zoldsegleves :bool = False
husleves :bool = False
gyumolcsleves :bool = False

foetel :int = None
foetelszoveg :str = None
sultCsirkecomb :bool = False
sultCsirkemell :bool = False
rakottzoldseg :bool = False
spagetti :bool = False
pizza :bool = False

koret :int = None
koretszoveg :str = None
rizs :bool = False
paroltzoldseg :bool = False
gyumolcs :bool = False
sultkrumpli :bool = False
salata :bool = False
kola :bool = False

ertekeles :str = None

print("Előétel\n1-Zöldségleves\n2-Húsleves\n3-Gyümölcsleves\n4-Semmi\nMit választ: ",end='')
eloetel = int(input())
if eloetel == 1:
    zoldsegleves = True
    eloetelszoveg = "Zöldségleves"

elif eloetel == 2:
    husleves = True
    eloetelszoveg = "Húsleves"

elif eloetel == 3: 
    gyumolcsleves = True
    eloetelszoveg = "Gyümölcsleves"

else:
    print("Semmi")
    eloetelszoveg = "Semmi"

print("Főétel:\n1-Sültcsirkecomb\n2-Sült csirkemell\n3-Rakottzöldség\n4-Spagetti\n5-Pizza\n6-Semmi\nMit választ: ",end='')
foetel = int(input())
if foetel == 1:
    sultCsirkecomb = True
    foetelszoveg = "Sültcsirkecomb"

elif foetel == 2:
    sultCsirkemell = True
    foetelszoveg = "Sült csirkemell"

elif foetel == 3: 
    rakottzoldseg = True
    foetelszoveg = "Rakottzöldség"

elif foetel == 4: 
    spagetti = True
    foetelszoveg = "Spagetti"

elif foetel == 5: 
    pizza = True
    foetelszoveg = "Pizza"

else:
    print("Semmi")
    foetelszoveg = "Semmi"

print("Köret:\n1-Rizs\n2-Pároltzöldség\n3-Gyümölcs\n4-Sültkrumpli\n5-Saláta\n6-Kóla\n7-Semmi\nMit választ: ",end='')
koret = int(input())
if koret == 1:
    rizs = True
    koretszoveg = "Rizs"

elif koret == 2:
    paroltzoldseg = True
    koretszoveg = "Pároltzöldség"

elif koret == 3: 
    gyumolcs = True
    koretszoveg = "Gyümölcs"

elif koret == 4: 
    sultkrumpli = True
    koretszoveg = "Sültkrumpli"

elif koret == 5: 
    salata = True
    koretszoveg = "Saláta"

elif koret == 6: 
    kola = True
    koretszoveg = "Kóla"

else:
    print("Semmi")
    koretszoveg = "Semmi"

system('cls')
# -	zöldségleves, spagetti, gyümölcs vagy saláta, nem lehet pizza, rakottzöldség
if (zoldsegleves and spagetti and (gyumolcs or salata) and ((pizza != True) or (rakottzoldseg != True))):
    ertekeles = "Kiváló"

# zöldségleves, sült csirkemell, és biztos nem tartalmaz sültkrumplit, de rizst igen
elif(zoldsegleves and sultCsirkemell and (sultkrumpli != True) and rizs):
    ertekeles = "Fittnesz menü"

# húsleves, sült csirkecomb, sültkrumpli és saláta, és biztosan nincs pizza, rakottzöldség
elif (husleves and sultCsirkecomb and (sultkrumpli or salata) and (pizza != True and rakottzoldseg != True)):
    ertekeles = "Vasárnapi menü"

# pizza vagy spagetti, gyümölcs, kóla a kínálatban és biztosan nincs rakottzöldség, pároltzöldség
elif ((pizza or spagetti) and (gyumolcs or kola) and (rakottzoldseg != True and paroltzoldseg != True)):
    ertekeles = "Napi menü"

#Semmi
elif ((eloetel >= 5) and (foetel >= 6) and (koret >= 7)):
    ertekeles = "Semmi"

#Egyéni
else:
    ertekeles = "Egyéni"

print(f"A mai menü értékelése: {ertekeles}")
print(f"A mai menü tartalma: {eloetelszoveg}, {foetelszoveg}, {koretszoveg}")