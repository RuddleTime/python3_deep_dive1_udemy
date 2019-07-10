
class Rectangle:
    def __init__(self, width, height):
        self.width = width 
        self.height = height

    # Getter method
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive')
        else:
            self._height = height 

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.height == other.height and self.width == other.width
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

"""
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
"""

r3 = Rectangle(10, 20)
print(r3)
# r3.width = -100
print(r3.width)
