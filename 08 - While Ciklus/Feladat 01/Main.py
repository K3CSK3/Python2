number :float = -1
temporary :str = None
isNumber :bool = False
converter :float = None

while (number < 0 or number > 10):
    print("Adjon meg egy számot 0 és 9 között: ",end="")
    temporary = input()
    temporaryCopy = temporary.replace(".", "").replace("-", "")
    isNumber = temporaryCopy.isnumeric()
    if (isNumber):
        number = int(temporary)
    else:
        print("Nem számot adott meg!")
print(number)