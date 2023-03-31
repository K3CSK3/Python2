from InOut import *

def bekeres(db:int) -> str:
    teljes :str = ''
    for i in range(1, db+1, 1):
        name = inOutName()
        hour = inOutHour()
        teljes += str(name) + ";" + str(hour) + "|"
    return(teljes)

def oraberSzamlalasKomplex(adat:str,db:int) -> str:
    for i in range(1, db+1, 1):   
        globals()['Munkas'+str(i)] = adat.split('|')[i-1]
    for i in range(1, db+1, 1):
        globals()['MunkasPenz'+str(i)] = int(globals()['Munkas'+str(i)].split(';')[1])
    for i in range(1, db+1, 1):
        if (globals()['MunkasPenz'+str(i)] <= 40):
            globals()['MunkasPenz'+str(i)] *= 1000
        else:
            globals()['MunkasPenz'+str(i)] = 40000 + ((int(globals() ['MunkasPenz'+str(i)]) - 40)*1500)
    teljes :str = ''
    for i in range(1,db+1,1):
        teljes += globals()['Munkas'+str(i)].split(';')[0] + ' ennyit keresett:'+ str(globals()['MunkasPenz'+str(i)]) + 'Ft' +('\n')
    return teljes
    


def oraberSzamlalas(adat:str) -> str:
    munkas1 = adat.split('|')[0]
    munkas2 = adat.split('|')[1]
    munkas3 = adat.split('|')[2]
    munkas4 = adat.split('|')[3]
    munkas5 = adat.split('|')[4]  

    ora1 = int(munkas1.split(';')[1])
    ora2 = int(munkas2.split(';')[1])
    ora3 = int(munkas3.split(';')[1])
    ora4 = int(munkas4.split(';')[1])
    ora5 = int(munkas5.split(';')[1])

    if (ora1 <= 40):
        munkas1Penz = int(munkas1.split(';')[1])*1000
    else:
        munkas1Penz = 40000 + ((int(munkas1.split(';')[1]) - 40)*1500)
    if (ora2 <= 40):
        munkas2Penz = int(munkas2.split(';')[1])*1000
    else:
        munkas2Penz = 40000 + ((int(munkas2.split(';')[1]) - 40)*1500)
    if (ora3 <= 40):
        munkas3Penz = int(munkas3.split(';')[1])*1000
    else:
        munkas3Penz = 40000 + ((int(munkas3.split(';')[1]) - 40)*1500)
    if (ora4 <= 40):
        munkas4Penz = int(munkas4.split(';')[1])*1000
    else:
        munkas4Penz = 40000 + ((int(munkas4.split(';')[1]) - 40)*1500)
    if (ora5 <= 40):
        munkas5Penz = int(munkas5.split(';')[1])*1000
    else:
        munkas5Penz = 40000 + ((int(munkas5.split(';')[1]) - 40)*1500)
    
    teljes = munkas1.split(';')[0] + ' ennyit keresett:'+ str(munkas1Penz) + 'Ft' + (',') + munkas2.split(';')[0] + ' ennyit keresett:'+ str(munkas2Penz) + 'Ft' + (',') + munkas3.split(';')[0] + ' ennyit keresett:'+ str(munkas3Penz) + 'Ft' + (',') + munkas4.split(';')[0] + ' ennyit keresett:'+ str(munkas4Penz) + 'Ft' + (',') + munkas5.split(';')[0] + ' ennyit keresett:'+ str(munkas5Penz) + 'Ft'

    return teljes