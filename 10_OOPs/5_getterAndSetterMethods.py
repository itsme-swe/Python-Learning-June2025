class Rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, len):
        if len >= 0:
            self._length = len
        else:
            self._length = 1

    @property
    def breadth(self):
        return self._breadth

    @breadth.setter
    def breadth(self, bre):
        if bre >= 0:
            self._breadth = bre
        else:
            self.breadth = 1

    def area(self):
        return self.length * self.breadth


r1 = Rectangle(10, 20)

print(r1.length)  # 10

r1.length = 30

print(r1.length)  # 30

print(r1.breadth)  # 20
