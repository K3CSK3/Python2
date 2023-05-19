from typing import *
from tanuloIO import *
from modell.tanulo import *

tanulo :List[Tanulo] = tanuloBekeres()
for line in tanulo:
    print(line)