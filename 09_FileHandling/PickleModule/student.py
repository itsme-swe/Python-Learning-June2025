class Student:

    def __init__(self, name, rollNo, dept):
        self.name = name
        self.rollNo = rollNo
        self.dept = dept

    def display(self):
        print(f"Name: {self.name}\n RollNo: {self.rollNo}\n Dept: {self.dept}")
