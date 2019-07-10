import ctypes
import gc  # garbage collection module

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    # Go through every object in the garbage collector
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists in gc"
    return "Not found"

a = [1, 2, 3]
z = 'random'
ref_count(id(a))

print(object_by_id(id(a)))
print(object_by_id(id(z)))


# Creating two classes to create a circular reference
class A:
    def __init__(self):
        self.b = B(self)
        # When the class instantiates itself, the memory 
        # addresses of the instance of A and instance of B
        print('A: self: {0}, b: {1}'.format(
            hex(id(self)), hex(id(self.b)))
        )

class B:
    def __init__(self, a):
        self.a = a    
        # Printing internal variable a below
        print('B: self: {0}, a: {1}'.format(
            hex(id(self)), hex(id(self.a)))
        )

# XXX disabling garbage collector
gc.disable()

my_var = A()

print('Memory address of \'my_var\'.b: {0}'.format(hex(id(my_var.b))))
print('Memory address of \'my_var\'.b.a: {0}'.format(hex(id(my_var.b.a))))


a_id = id(my_var)
b_id = id(my_var.b)

print("Ref count for a_id: {0}".format(ref_count(a_id)))
print("Ref count for b_id: {0}".format(ref_count(b_id)))

print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None


print("*****************Setting \'a\' to None*****************")

print("Ref count for a_id: {0}".format(ref_count(a_id)))
print("Ref count for b_id: {0}".format(ref_count(b_id)))

print(object_by_id(a_id))
print(object_by_id(b_id))

# Running garbage collector manually
gc.collect()
print("*****************Running gc manually *****************")

print("Ref count for a_id: {0}".format(ref_count(a_id)))
print("Ref count for b_id: {0}".format(ref_count(b_id)))

print(object_by_id(a_id))
print(object_by_id(b_id))
