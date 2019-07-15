
def process(t):
    t[0].append(3)

my_tuple = ([1, 2], 'a')

# XXX: Even though tuples are immutable, since one of the tuples elements
# (i.e. a List), is mutable, the contents of the tuple change
print(my_tuple)
print(id(my_tuple))
process(my_tuple)
print(my_tuple)
print(id(my_tuple))
print(id(my_tuple[0]))
