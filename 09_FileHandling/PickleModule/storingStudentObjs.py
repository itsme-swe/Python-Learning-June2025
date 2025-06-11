import student, pickle

studentLst = [
    student.Student("Harsh", 105, "full-stack"),
    student.Student("Mukul", 115, "backend"),
    student.Student("HarshKasliwal", 205, "Finance"),
]

with open("studentsData.txt", "wb") as sd:
    for s in studentLst:
        pickle.dump(s, sd)
