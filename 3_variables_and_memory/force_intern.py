import sys
import time


print('Before interning')
a = "When we were young ... in a land of miracles"
b = "When we were young ... in a land of miracles"
# Due to Python optimisations the below will result in Ture
# However this will be False if run via Python interactive mode
print(a is b)
print(id(a), id(b))

a = sys.intern("In the place we lived ...")
b = sys.intern("In the place we lived ...")

# Since a and b have been interned, the identity operator can be 
# used over the equality operator to compare the strings, which
# is much faster
print("\nAfter interning")
print(a is b)
print(id(a), id(b))




def using_identity_operator(n):
    a = sys.intern('long not interned string' * 200)
    b = sys.intern('long not interned string' * 200)
    for i in range(n):
        if a is b:
            pass
    

def using_equality_operator(n):
    a = 'long not interned string' * 200
    b = 'long not interned string' * 200
    for i in range(n):
        if a == b:
            pass

n = 10000000

start = time.perf_counter()  # number of milliseconds
using_equality_operator(n)
end = time.perf_counter()
print("Time to run with equality operator: {0}ms".format(end - start))

start = time.perf_counter()
using_identity_operator(n)
end = time.perf_counter()
print("Time to run with identity operator: {0}ms".format(end - start))

