class Rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    @staticmethod
    def cal_area(length, breadth):
        return length * breadth


print(Rectangle.cal_area(10, 5))
