"""
Udemy course: Python 3: Deep Dive (Part 1)
Section 4: Numeric Types
Part 35-42: Floats
"""

import math

# A float uses a fixed number of bytes (normally 8 bytes), unlike ints. 
# Bits are divided up by:
# 1. One bit is used for the sign +(0) or -(1) of the float
# 2. 11 bits are used for the exponent (eg. 1.5E-5 -> -5 is the exponent)
# 3. Signigicant digits

# Valide ways of initising a float
a = float(10)
b = float(10.4)
c = float("12.5")

# Looking at issue where a number (eg. 0.1) is finite in base 10 
# but not so in base 2
x = 0.1
print("Printing \'{0}\' with increased expansion:".format(x))
print(format(x, '.15f'))
print(format(x, '.25f'))

# Looking at when a number is finite in binary
x = 0.125
print("Printing \'{0}\' with increased expansion:".format(x))
print(format(x, '.15f'))
print(format(x, '.25f'))

# Example of why knowledge of precision in binary is important:
x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)  # Will be False
print((format(x, '.25f'), format(y, '.25f')))
x = 0.125 + 0.125 + 0.125
y = 0.375
print(x == y)  # Will be True
print((format(x, '.25f'), format(y, '.25f')))

# To resolve the above, can set an eipsolon range the the numbers
# need to fall within, in order to be considered equal
# -> Better to say the numbers are within a percentage of each other

# Pep 485 documenation goes into detail on this
# Use math.isclose method 

# Looking at range/epilson (absolute values) approach
x = 0.1 + 0.1 + 0.1
y = 0.3
print((format(x, '.20f'), format(y, '.20f')))
diff = format(x - y, '.20f')
print(diff)

# To compare floating point numbers do not use == use math.isclose method
x = 1000.01
y = 1000.02
check_same = math.isclose(x, y, rel_tol=1e-5, abs_tol=1e-5)
print(check_same)  # Prints True

x = 0.01
y = 0.02
check_same = math.isclose(x, y, rel_tol=1e-5, abs_tol=1e-5)
print(check_same)  # Prints False



# Coercing float to int, which will result in data loss
# Python options: truncation, floor, ceiling, rounding

# Truncation: returns int potion of number
print(math.trunc(-10.5))  # Prints -10 -> same as int(-10.5)

# Floor: Largest int <= the number
print(math.floor(10.5))  # Prints 10
print(math.floor(-10.5))  # XXX: Prints -11

# Ceiling: Smallest int >= the number
print(math.ceil(10.5))  # Prints 11
print(math.ceil(-10.5))  # XXX: Prints -10









