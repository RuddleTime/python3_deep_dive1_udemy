"""
Udemy course: Python 3: Deep Dive (Part 1)
Section 4: Numeric Types
Part 29: Intergers: Data Types 
"""

import sys
import time

integer = 100
print("{0} is {1} and uses {2} memory".format(
    integer,
    type(integer),
    sys.getsizeof(integer)  # Get size of memory used to store variable
))

integer = 0
print("{0} is {1} and uses {2} memory".format(
    integer,
    type(integer),
    sys.getsizeof(integer)  # Get size of memory used to store variable
))

rational = (1 / 2)
print("{0} is {1} and uses {2} memory".format(
    rational,
    type(rational),
    sys.getsizeof(rational)
))

real = 100.678
print("{0} is {1} and uses {2} memory".format(
    real,
    type(real),
    sys.getsizeof(real)
))

complex_num = complex(100, 2)
print("{0} is {1} and uses {2} memory".format(
    complex_num,
    type(complex_num),
    sys.getsizeof(complex_num)
))

boolean = True
print("{0} is {1} and uses {2} memory".format(
    boolean,
    type(boolean),
    sys.getsizeof(boolean)
))

# Confirming calculations with large numbers are slower
def calc(a):
    for i in range(10000000):
        a * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end - start)




