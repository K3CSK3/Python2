from os import system

month :str = None

print("Adja meg egy hónap nevét(pl:Január)",end='')
month = input().strip().lower()

system('cls')

match month:
    case "Január":
        print("Ez az 1. hónap")
    case "Február":
        print("Ez az 2. hónap")
    case "Március":
        print("Ez az 3. hónap")
    case "Április":
        print("Ez az 4. hónap")
    case "Május":
        print("Ez az 5. hónap")
    case "Június":
        print("Ez az 6. hónap")
    case "Július":
        print("Ez az 7. hónap")
    case "Augusztus":
        print("Ez az 8. hónap")
    case "Szeptember":
        print("Ez az 9. hónap")
    case "Október":
        print("Ez az 10. hónap")
    case "November":
        print("Ez az 11. hónap")
    case "December":
        print("Ez az 12. hónap")
    case _:
        print("Nincs ilyen hónap")