class Parent:

    def show(self):
        print("Parent show")


class Child(Parent):

    def show(self):
        print("Child show")


c = Child()

c.show()  # Child show

print(Child.mro())  
# [<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>]


# 💥 MRO stands for Method Resolution Order. It is the order in which Python looks for a method in a hierarchy of classes.