
class Rectangle:
    # Initialiser - Runs when the object is created
    # First arguement of this method is the object itself (
    # by convention this is named 'self'
    def __init__(self, width, height):
        # Setting value attributes of the class
        # Class properties are width and height
        
        self.width = width 
        self.height = height


    # This is an instance method, which is callable
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    # Overwritting 'str' to return our string method
    def __str__(self):
        # Getting string repesentation of object
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    # Represenation method
    def __repr__(self):
        # Typically a string that shows how you would build
        # the object up again
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    # This is an instance method
    def __eq__(self, other):
        # Note in the way this is called below, r1 will be passed into 
        # the self object, and r2 will be passed into the 'other' object.
        
        # Need to ensure that other is in fact an instance of Rectangle
        if isinstance(other, Rectangle):
            return self.height == other.height and self.width == other.width
        else:
            return False

    # Overwritting the built in 'less than' Python operation
    # Less than is a binary operation (i.e. takes two arguements)
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented



# Creating an instance of the Rectangle class
r1 = Rectangle(10, 20)

# Can query the width etc. 
print(r1.width) 

# Calling an instance method of the Rectangle class
print("Area of rectangle: {0}".format(r1.area()))
print("Perimeter of rectangle: {0}".format(r1.perimeter()))
       
# Memory address of object
print(hex(id(r1))) 

r2 = Rectangle(10, 200)
# Note below, calling 'str' function below, returns our __str__ method,
# not the built in Python 'str' function
print(str(r2))

# The below is calling on the __repr__ method in the Rectangle class
print(Rectangle(10, 20))

# The below will be False, as they are different memory addresses
# However as we have defined an __eq__ method in the Retangle class
# this is now return True, as the build in Python equality function 
# has been overwritten
print('Are the rectangels equal?: {0}'.format(r1 == r2))


print('Is r1 less than r2?: {0}'.format(r1 < r2))

# Even though we have not overwritten the gt method, we
# can still call it and it will check if the lt method has been written
# and use the reverse output of that
print('Is r1 less than r2?: {0}'.format(r1 > r2))
