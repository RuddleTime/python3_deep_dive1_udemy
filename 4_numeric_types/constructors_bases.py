"""
Udemy course: Python 3: Deep Dive (Part 1)
Section 4: Numeric Types
Part 31 & 32: Constructors and Bases 
"""

# Int constructor takes two constructors (second one optional)
# 1. Numerical value or string that parse to number
# 2. Optional: Number Base

# Going from different bases to base 10

print("{0} is equal to {1}".format(
    "int(\"1010\", base=2)",
    int("1010", base=2)
))
print("{0} is equal to {1}".format(
    "int(\"A12F\", base=16)", int("A12F", base=16)
))
print("{0} is equal to {1}".format(
    "int(\"534\", base=8)",
    int("534", base=8)
))
print("{0} is equal to {1}".format(
    "int(\"A\", base=11)",
    int("A", base=11)
))

# Going from base 10 to different bases

# Base Two will be prefixed with '0b' to indicate binary
print("{0} is equal to {1} in binary".format("bin(10)", bin(10)))

# Base Eight - Prefixed with '0o'
print("{0} is equal to {1} in base eight".format("oct(10)", oct(10)))

# Base 16 - Prefixed with '0x'
print("{0} is equal to {1} in base sixteen".format("hex(10)", hex(10)))


# Converting to bases not pre-coded into Python

def from_base10(n, b):
    """
    n = number to be trasformed 
    b = base to be transformed into
    """
    if b < 2:
        raise ValueError("Base must be greater than 2")
    if n < 0:
        raise ValueError("Number must be positive")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, mod = divmod(n, b)  # divmod function returns tuple of (div, mod)
        digits.insert(0, mod)
    return digits

print(from_base10(333, 3))
print(from_base10(534, 8))
print(from_base10(10, 8))
print(from_base10(255, 16))

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not long enough to encode digits')
    encoding = ''.join([digit_map[d] for d in digits])
    return encoding

print(encode(from_base10(255, 16), '0123456789ABCDEF'))
