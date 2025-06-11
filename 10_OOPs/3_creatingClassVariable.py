class Rectangle:

    count = 0

    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        Rectangle.count += 1

    def area(self):
        return self.length * self.breadth

    @classmethod
    def get_count(cls):
        return cls.count


r1 = Rectangle(10, 10)
r2 = Rectangle(20, 5)

print(Rectangle.get_count())  # 2 -- this is the count of objects created upon the class
