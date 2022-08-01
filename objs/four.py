class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Student:
    def __init__(self, studentName, enrolled):
        self.studentName = studentName
        self.GPA = 0.0
        self.creditHours = 0
        self.enrolled = enrolled
        self.classes = []

newStudent=Student(Name("atleen", "jose"), True)
# newName=Name("atleen", "jose")
# newStudent=Student(newName, True)
# newStudent=Student("atleen jose", True)

