from os import system

resistance1 :int = None
resistance1 :int = None
connectionType :str = None

print("Adja meg az egyik ellenállás értékét: ",end='')
resistance1 = int(input().strip())
print("Adja meg a másik ellenállás értékét: ",end='')
resistance2 = int(input().strip())
print("Adja meg a kötés típusát: ",end='')
connectionType = input().strip().lower()

system('cls')

match connectionType:
    case "p":
        print((resistance1*resistance2)/(resistance1+resistance2))
    case "s":
        print(resistance1+resistance2)