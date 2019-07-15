
def square(a):
    return a ** 2

print("Type of function: {0}".format(type(square)))
print("Memory ID of function: {0}".format(id(square)))

f = square
print("Memory ID of variable f: {0}".format(id(f)))



""" Function returing function """

def cube(a):
    print('Start of cube function')
    return a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

fn = select_function(2)
print(fn)
print("Identity operator: {0}".format(fn is square))
print("Identity operator: {0}".format(fn is cube))

# Below call will invoke cube function
print(fn(2))
# Selecting the cube function and passing it the value of three
print(select_function(2)(3))


""" Passing function to function """

def exec_function(fn, n):
    print('\nStart of exec function')
    return fn(n)

print(exec_function(cube, 3))
