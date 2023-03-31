from functions import *
from InOut import *

konvertTo = inOutCurrency()
money = inOutMoney()

vegosszeg = konvertalo(money, konvertTo)

print(vegosszeg)