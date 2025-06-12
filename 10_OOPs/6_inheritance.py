# 💥 Parent Class
class Rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# 💥 Child Class
class Cuboid(Rectangle):

    def __init__(self, l, b, h):
        self.height = h
        super().__init__(l, b)
        # By using super() keyword we are calling __init__() method of parent class in chaild class

    def volume(self):
        return self.length * self.breadth * self.height


c = Cuboid(10, 5, 5)

print(c.volume())  # 250
