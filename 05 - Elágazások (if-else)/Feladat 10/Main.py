from os import system
number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if ((number % 3 and number % 2) == 0):
    print("ZIZI")
elif ((number % 2) == 0):
    print("BAZ")
elif ((number % 3) == 0):
    print("BIZ")
else:
    print("A szám nem osztható 2-vel se 3-al se")