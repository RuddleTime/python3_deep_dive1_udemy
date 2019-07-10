
class Rectangle:
    def __init__(self, width, height):
        # Setting width and heigth to be private variables, sign to 
        # other users that they should not change the variables (however this
        # is only a convention and the variables can be changed)

        # We are doing this here, to encourage people not to set the width and 
        # height directly, but to set them via the getters and setters 
        self._width = width 
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width): 
        if width <= 0:
            raise ValueError('Value of width must be positive.')
        else:
            self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height): 
        if height <= 0:
            raise ValueError('Value of height must be positive.')
        else:
            self._height = height 

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return (self._width + self._height) * 2

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._height == other._height and self._width == other._width
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)

# Memory address of object
print(hex(id(r1))) 

r2 = Rectangle(10, 200)
print(str(r2))

# The below is calling on the __repr__ method in the Rectangle class
print(Rectangle(10, 20))

print('Are the rectangels equal?: {0}'.format(r1 == r2))

print('Is r1 less than r2?: {0}'.format(r1 < r2))

print('Is r1 less than r2?: {0}'.format(r1 > r2))


print(r1)
print(r1.get_width())
r1.width = -100
print(r1.width)
r1.set_width(5)
print(r1._width)


