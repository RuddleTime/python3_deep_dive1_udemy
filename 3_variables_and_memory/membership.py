"""
Looking at constant expressions i.e. they
will not change over the lifetime of the code
https://www.udemy.com/python-3-deep-dive-part-1/learn/lecture/7368672#questions/6221422
"""

import pprint
import inspect

import string
import time

def my_func():
    # Python precalculates and stores items that
    # are 20 or less characters long
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11  # This is more than 20 characters
    e = 'Beyond the horizon ...' * 5  # >20
    # A list is mutable, so below will not be precalculated
    f = ['a', 'b'] * 3  

# Looking at property that contaions all the constants
# associated with the function after it has been complied
pprint.pprint(my_func.__code__.co_consts)
# Printing contents of function for easy comparision with above output
print(inspect.getsource(my_func))  


"""
Looking at membership tests
"""


def membership_tests(e):
    if e is {1, 2, 3}:
        pass

# If the below is run in python interactive the following would be returned:
# (None, 1, 3, frozenset({1, 3})) 
# So the set {1, 2, 3} has been converted to a frozenset
# A list would be converted into a tuple
pprint.pprint(membership_tests.__code__.co_consts)


# XXX: Note set membership checks are much quicker than lists or
#      tuple membership checks
# Preforming timing test to illistrate this

all_char_list = list(string.ascii_letters)
all_char_tuple = tuple(string.ascii_letters)
all_char_set = set(string.ascii_letters)

def membership_test(n, container):
    """
    n: number of times to test for membership
    """
    for i in range(n):
        if 'z' in container:
            pass

n = 10000000
start = time.perf_counter()
membership_test(n, all_char_list)
end = time.perf_counter()
print('Time of list membership test: {0}ms'.format(end - start))

start = time.perf_counter()
membership_test(n, all_char_tuple)
end = time.perf_counter()
print('Time of tuple membership test: {0}ms'.format(end - start))

start = time.perf_counter()
membership_test(n, all_char_set)
end = time.perf_counter()
print('Time of set membership test: {0}ms'.format(end - start))

