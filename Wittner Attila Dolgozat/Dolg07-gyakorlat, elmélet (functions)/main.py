from consoleIO import *
from services import *

#mik ezek az also vonalak a nevekben !!!!!!!!!!!!!!!!!!!!!!!
#ki tanitja ezt neketek ??????
#valtozok tipusa nincs definialva

nev = nev_bekeres() 
oraszam = oraszam_bekeres()
tulora = tulora_bekeres()

ber = oraber_kalkulator(oraszam,tulora)

kiiras(nev,ber)