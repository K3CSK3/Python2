from os import system

numberOne :int = None
numberTwo :int = None
numberThree :int = None

print("Adjon meg egy számot: ",end='')
numberOne = int(input())

print("Adjon még egy számot: ",end='')
numberTwo = int(input())

print("Adjon egy harmadik számot: ",end='')
numberThree = int(input())

system('cls')

if (numberOne > numberTwo and numberOne > numberThree and numberTwo > numberThree):
    print(numberOne,numberTwo,numberThree) #1,2,3

elif (numberOne > numberTwo and numberOne > numberThree and numberThree > numberTwo):
    print(numberOne,numberThree,numberTwo) #1,3,2


elif (numberTwo > numberOne and numberTwo > numberThree and numberOne > numberThree):
    print(numberTwo,numberOne,numberThree) #2,1,3

elif (numberTwo > numberOne and numberTwo > numberThree and numberThree > numberOne):
    print(numberTwo,numberThree,numberOne) #2,3,1

elif (numberThree > numberOne and numberThree > numberTwo and numberTwo > numberOne):
    print(numberThree,numberTwo,numberOne) #3,2,1

elif (numberThree > numberOne and numberThree > numberTwo and numberOne > numberTwo):
    print(numberThree,numberOne,numberTwo) #3,1,2