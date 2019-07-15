
""" Comparing ints """

a = 10
b = 10

print("Identity operator on ints: {0} IDs: {1}, {2}".format(a is b, id(a), id(b)))
print("Equality operator on ints: {0}".format(a == b))


""" Comparing stings """

a = 'boo'
b = 'boo'

print("Identity operator on strings: {0} IDs: {1}, {2}".format(a is b, id(a), id(b)))
print("Equality operator on strings: {0}".format(a == b))


""" Comparing lists """

# XXX: a and b will not have a shared reference as lists are mutable
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

print("Identity operator on lists: {0} IDs: {1}, {2}".format(a is b, id(a), id(b)))
print("Equality operator on lists: {0}".format(a == b))


""" Comparing int and float"""

a = 10
b = 10.0

print("Identity operator on int Vs float: {0} IDs: {1}, {2}".format(a is b, id(a), id(b)))
print("Equality operator on int Vs float: {0}".format(a == b))
