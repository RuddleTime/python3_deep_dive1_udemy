

def process(lst):
    lst.append(100)
    return lst

my_list = [1, 2, 3]

print(my_list)
result = process(my_list)

# XXX: Both of the below will be the same, as lists are mutable
print(result)
print(my_list)
