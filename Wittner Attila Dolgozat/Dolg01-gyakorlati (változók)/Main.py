from os import system

name :str = None
brand :str = None
model : str = None
year : int = None
price : float = None


print("\nA vevő bemegy az autókereskedésbe és bemutatkozik.\n")
name = input()

print(f"\nJó napot kedves {name} Miben segíthetek")
print(f"\nÉrdekelne egy: ",end='')
brand = input()

print(f"\nÉrtem, egy {brand}. Melyik modell?\n")
model = input()

print("\nÉvjárat?\n")
year = input()

print("\nHány milliót szánna rá?\n")
price = input()


system('cls')

print(f"Sajnálom kedves {name}, de jelenleg {year}-es évjáratú és {brand} {model} nincs a kínálatunkban ami beleférne a {price} millió forintba.\n")