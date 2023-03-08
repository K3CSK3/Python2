from os import system

number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if ((number > 10 and number < 20) or (number < -10 and number > -20)):
    print(f"A szám {number} 10 és 20 vagy -10 és -20 között van")
else :
    print(f"A szám {number} nincs rajta a 10,20-as vagy a -10,-20-as szakaszon")