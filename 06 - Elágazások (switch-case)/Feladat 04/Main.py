from os import system

number1 :int = None
number2 :int = None
operation :int = None

print("Adjon meg egy számot:",end='')
number1 = int(input().strip())
print("Adjon meg még egy számot:",end='')
number2 = int(input().strip())
print("Adjon meg egy műveleti jelet:",end='')
operation = input().strip()

system('cls')

match operation:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * number2)
    case "/":
        print(number1 / number2)
    case "_":
        print("Nincs ilyen műveleti jel!")
