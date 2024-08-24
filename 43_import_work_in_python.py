# Importing in python is the process by which we can load the functions from the module in the python script
# we can load the functions and the variables from the module to the python script
# once the model is imported in the python script we can use the functions and variables of the module using python script

import math
from math import pi
result=math.sqrt(9)* pi
print(result)


# we can import all the functions and variables from the module using the *(wildcard) but this method is not recommended because it creates complexity when we have same constants in two modules
import math
from math import *
result=math.sqrt(67) * pi
print(result)

import math 
from math import pi, sqrt as s
result=s(9)*pi
print(result)

import math as m
result=m.sqrt(9)*m.pi
print(result)

import math
print(dir(math))
print(math.floor, type(math.floor))

import math as math_builtin_function
from math import pi, sqrt 
result=math_builtin_function.sqrt(9)*math_builtin_function.pi
print(result)

from maria import welcome, maria
welcome()
print(maria)
import maria as mr
mr.welcome()
print(mr.maria)