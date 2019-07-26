"""
Udemy course: Python 3: Deep Dive (Part 1)
Section 4: Numeric Types
Part 32-33: Rational Numbers 
"""

from fractions import Fraction
# Fraction class in Python is used to represent Rational numbers

x = Fraction(3, 4)  # 3/4
print(x)

# Note: Fractions are automatically reduced by the fraction class
a = Fraction(5, 10)
b = Fraction(1, 2)

print(a == b)  # Equates to True
print(a is b)  # Equates to False 

# Python will put the negitive sign with the numerator

neg_x = Fraction(3, -4)
print(neg_x)  # prints -3/4

# Passing in string 

str_x = Fraction('0.125')
print(str_x)  # prints 1/8
str_x = Fraction('22/7')
print(str_x)  # prints 22/7

# Seperating out the numerator and denominator of fractions

x = Fraction(3, 4)
print(x.numerator)  # prints 3
print(x.denominator)  # prints 4

# In Python, any float can be witten as a fraction as it
# has a finite precision

# Looking at irrational numbers
import math
x = Fraction(math.pi)
print(x)  # prints 884279719003555/281474976710656
x = Fraction(math.sqrt(2))
print(x)  # prints 6369051672525773/4503599627370496 


# Constraining the denominator

print("\nRepresenting Pi")
x = Fraction(math.pi)
print(x.limit_denominator(10))  # denominator is to be no greater than 10
print(float(x.limit_denominator(4)))
print(x.limit_denominator(4))
print(float(x.limit_denominator(10)))
print(x.limit_denominator(10))
print('\n')

 
