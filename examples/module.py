a = 2
b = 3

# Import module as namespace
import math_module
math_module.sum(a, b)

# Import all modules into current namespace
from math_module import *
sub(a, b)
mul(a, b)

# Import specific items into current namespace
from math_module import div, exp
div(a, b)
exp(a, b)

