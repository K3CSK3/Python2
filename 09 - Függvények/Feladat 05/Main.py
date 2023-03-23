from functions import *
from InOut import *

word01 = elsoInOut().lower()
word02 = masodikInOut().lower()

egyezik = osszehasonlito(word01, word02)

kiiras(word01, word02, egyezik)