import sys
import ctypes

a = [1, 2, 3]
b = 2
c = a

# Printing out memory addresses
print('Memory address of \'a\': {0} or {1}'.format(id(a), hex(id(a))))
print('Memory address of \'b\': {0} or {1}'.format(id(b), hex(id(b))))
print('Memory address of \'c\': {0} or {1}'.format(id(c), hex(id(c))))

# Getting number of references to that memory address
# Note: Useing 'getrefcount' will in itself create another reference
print('Reference count of \'a\': {0}'.format(sys.getrefcount(a)))
print('Reference count of \'b\': {0}'.format(sys.getrefcount(b)))
print('Reference count of \'c\': {0}'.format(sys.getrefcount(c)))

# Passing in memory address to find the number of references
print('Refcount of \'a\' using \'from_address\': {0}'.format(
    ctypes.c_long.from_address(id(a)).value)
)
print('Refcount of \'b\' using \'from_address\': {0}'.format(
    ctypes.c_long.from_address(id(b)).value)
)
print('Refcount of \'c\' using \'from_address\': {0}'.format(
    ctypes.c_long.from_address(id(c)).value)
)
