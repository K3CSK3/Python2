from os import system

number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if ((number % 4 and number % 6) == 0):
    print("Nem osztható néggyel és hattal(maradék nélkül)")
elif (number / 4 and number % 6):
    print("Csak nyéggyel osztható")
elif (number % 4 and number / 6):
    print("Csak hattal osztható")
else :
    print("Osztható hattal és néggyel")