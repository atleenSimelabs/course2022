class Student:
    def __init__(self) -> None:
        self.studentName=""
        self.GPA=0.0
        self.creditHours=0
        self.enrolled=True
        self.classes=[]

newStudent=Student()
newStudent.studentName="Atleen"
newStudent.GPA=9.8
newStudent.creditHours=9
newStudent.enrolled=True
newStudent.classes=["CHN", "KLA"]

print(newStudent.studentName)
print(newStudent.GPA)
print(newStudent.creditHours)
print(newStudent.enrolled)
print(newStudent.classes)


