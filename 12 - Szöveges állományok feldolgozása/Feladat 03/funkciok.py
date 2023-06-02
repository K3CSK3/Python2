from Jatekos import *
def posztKereso(jatekosok :list[Jatekos], poszt):
    visszateres: list[Jatekos] = []
    for jatekos in jatekosok:
        if (jatekos.poszt == poszt):
            visszateres.append(jatekos)
    return visszateres