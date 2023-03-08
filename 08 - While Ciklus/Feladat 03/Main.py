import random

szam :int = None
szam = (random.randrange(0, 9))
proba :int = 5
tipp :int = None

while (proba > 0 and tipp != szam):
    print(f"Gondoltam egy számra 0 és 9 között ({proba} próbálkozás)")
    tipp = int(input())
    proba -= 1

if (tipp == szam):
    print("Kitalálta")
else:
    print("Nem találta ki")