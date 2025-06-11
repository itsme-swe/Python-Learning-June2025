import student, pickle

with open("studentsData.txt", "rb") as f:

    for i in range(3):
        s = pickle.load(f)
        s.display()
