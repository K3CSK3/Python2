from Jatekos import *
def posztKereso(jatekosok :list[Jatekos], poszt):
    visszateres: list[Jatekos] = []
    
    for jatekos in jatekosok:
        if (jatekos.poszt == poszt):
            visszateres.append(jatekos)
    return visszateres

def magassagRendezo(jatekosok :list[Jatekos], sorrend):
    visszateres: list[Jatekos] = []
    darabszam = len(jatekosok)

    for i in range(0, darabszam, 1):
        for j in range(i+1, darabszam,  1):
            if ((jatekosok[j].magassag > jatekosok[i].magassag) and sorrend=="csökkenő"):
                ideiglenes = jatekosok[i].magassag
                jatekosok[i].magassag = jatekosok[j].magassag
                jatekosok[j].magassag = ideiglenes

            if ((jatekosok[j].magassag < jatekosok[i].magassag) and sorrend=="növekvő"):
                ideiglenes = jatekosok[i].magassag
                jatekosok[i].magassag = jatekosok[j].magassag
                jatekosok[j].magassag = ideiglenes
    return visszateres

def atlagnalMagasagabb(jatekosok :list[Jatekos]):
    osszMagassag: int = 0
    visszateres = []

    for jatekos in jatekosok:
        osszMagassag += int(jatekos.magassag)
    atlag = osszMagassag/len(jatekosok)
    for jatekos in jatekosok:
        if (float(jatekos.magassag) >= atlag):
            visszateres.append(jatekos)
    return visszateres

def atlagtolKisebb(jatekosok :list[Jatekos]):
    osszMagassag: int = 0
    visszateres = []

    for jatekos in jatekosok:
        osszMagassag += int(jatekos.magassag)
    atlag = osszMagassag/len(jatekosok)

    for jatekos in jatekosok:
        if (float(jatekos.magassag) <= atlag):
            visszateres.append(jatekos)
    return visszateres