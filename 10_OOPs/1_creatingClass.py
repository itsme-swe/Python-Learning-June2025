class Rectangle:

    def __init__(self):
        self.length = 10
        self.breadth = 20

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r1 = Rectangle()

print(f"Length: {r1.length}")

print(f"Breadth: {r1.breadth}")

print(f"Area: {r1.area()}")

print(f"Perimeter: {r1.perimeter()}")
