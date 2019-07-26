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

"""
Equality Testing
"""
print("\n\nEquality Testing\n")

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

"""
Coercing float -> int
"""
print('\n\nCoercing with trunc, floor and ceil\n')

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

"""
Rounding of floats
"""

# Use built in round(x, n=0) funtion
# x=number to be rounded
# n -> 10**-n

print('\n\nRounding\n')

print(round(10.4), type(round(10.4)))  # Prints 10, int
print(round(-10.4), type(round(-10.4)))  # Prints -10, int
print(round(10.8), type(round(10.8)))  # Prints 11, int
print(round(-10.8), type(round(-10.8)))  # Prints -11, int

# If n is specified, a float is returned
# The zero below is 10 to power of -0, so 1. Rounding to 
# powers of 10.
print(round(10.4, 0), type(round(10.4, 0)))  # Prints 10.0, float 

# Note: negitive n allows us to round to 10s, 100s, 1000s, etc.
#       positive n allows us to round to .1s, .01s, 0.001s, etc

# Looking at ties
x = 1.25  # Half way between 1.2 and 1.3
print(round(1.25, 1))  # Prints 1.2!!!!
print(round(1.35, 1))  # Prints 1.4
print(round(-1.25, 1))  # Prints -1.2
print(round(-1.35, 1))  # Prints -1.4

# XXX: The above is explained in IEEE 754 standard: round to the nearest
#      value, with ties rounded to the nearest value with an *even*
#      least significant digit 
#      This is called "Banker's Rounding"

"""
Force rounding to be away from zero
"""

# More correct way than standard of adding 0.5 and truncating
# Steps: 1. Take abs value
#        2. Add 0.5
#        3. Convert to int
#        4. Put back orginal sign

x = 10.25
rounded_x = math.copysign(1, x) * int(math.fabs(x)+0.5)
print(rounded_x)
# Simplier implementation:
def round_away_from_zero(x):
    return int(x + math.copysign(0.5, x))
rounded_x = round_away_from_zero(x)
print(rounded_x)
x = -10.5
rounded_x = round_away_from_zero(x)
print(rounded_x, round(-10.5))  # Prints -11, -10





