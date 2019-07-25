"""
Udemy course: Python 3: Deep Dive (Part 1)
Section 4: Numeric Types
Part 30: Intergers: Operations
"""

import math

# Divison will always return a Float

a = 6
b = 3

print("{0} of {1} / {2} of {3} results in {4} of {5}".format(
    a, type(a),
    b, type(b),
    a / b, type(a / b)
))

# To get the remainer of a divison use modulo (%)

# To get the whole number of the divsion but
# not the remainder use the floor division (//)

# Looking at positive example
a = 135
b = 4

floor = math.floor(a/b)  # same as: floor = a // b
modulo = a % b

c = (b * floor) + modulo
print(a==c)
print(a is c)
print("Floor: {0}".format(floor))
print("Modulo: {0}".format(modulo))
print(id(a), id(b)) 
print(a)
print(c)


# Looking at negative example (note the floor and 
# modulo will be different than above)
a = -135
b = 4

floor = a // b
modulo = a % b

c = (b * floor) + modulo
print(a==c)
print(a is c)
print("Floor: {0}".format(floor))
print("Modulo: {0}".format(modulo))
print(id(a), id(b)) 
print(a)
print(c)
