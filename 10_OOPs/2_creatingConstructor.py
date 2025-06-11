# 💥 In this class we are using default arguments inside constructor function "__init__" of python. Here 'self' keyword stands for current object


class Rectangle:

    def __init__(self, l=1, b=1):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth


rect1 = Rectangle(10, 5)
rect2 = Rectangle()
rect3 = Rectangle(10)

print(rect1.area())  # 50

print(rect2.area())  # 1

print(rect3.area())  # 10
