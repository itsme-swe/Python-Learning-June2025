class Parent:

    def show(self):
        print("Parent")


class Child(Parent):

    def show(self):
        super().show()  # This is how we call parent class method inside child class method
        print("Child")


c = Child()

c.show()

"""
Parent
Child
"""
