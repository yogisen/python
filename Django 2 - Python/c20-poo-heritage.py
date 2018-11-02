class Printable:
    def __init__(self):
        print("Calling Printable constructor")

    def print(self):
        print("Printing object", self.__class__.__name__)  # introspection to retrieve class Name


class Shape:
    def __init__(self):
        print("Calling Shape constructor")

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()  # calling parent function __init__()
        print("Calling Circle constructor")
        self.radius = radius

    # override parent function draw
    def draw(self):
        print("Drawing circle of radius", self.radius)


# Multiple inheritance
class Square(Shape, Printable):

    def __init__(self, size):
        # super().__init__()  # MRO (Method Resolution Order)

        # Call to all parent constructors
        Shape.__init__(self)
        Printable.__init__(self)
        print("Calling Square constructor")

        self.size = size

    def draw(self):
        print("Drawing square of size", self.size)


circle = Circle(10)
circle.draw()

square = Square(4)
square.draw()
square.print()
