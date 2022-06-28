# Import a module, use the module name
# together with the function name.
import math
print(math.sqrt(2))

# Import the module, give it an alias, use
# the alias together with the function name.
import math as m
print(m.sqrt(2))

# Import a function from a module, use the
# function name only.
from math import sqrt
print(sqrt(2))

# Import a function from a module, give the
# function name an alias, use the alias.
from math import sqrt as kvadratrot
print(kvadratrot(2))

# Import all functions from a module, use
# function names only.
from math import *
print(sqrt(2))

