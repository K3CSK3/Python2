from os import system

number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if (number > -30 and number < 40):
    print(f"A szám {number} -30 és 40 között van")
else :
    print(f"A szám {number} nincs rajta a -30, 40-es szakaszon")