class Parent:

    def __init__(self, d):
        self.__data = d

    def show(self):
        print(self.__data)




p = Parent(10)

p.show()  # 10

p.data = 20

p.show()  # 10

p._Parent__data = 30  # This is known as name mangling forceibly changing the private data of memeber of class

p.show()  # 30
