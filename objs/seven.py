class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

myPerson = Person(Name("David", "Joyner"), "brown", 30)
myPerson1=Person(myPerson.name, myPerson.eyecolor, myPerson.age)
myPerson1.eyecolor='blue'
print(myPerson.eyecolor)
print(myPerson1.eyecolor)
myPerson1.name.firstname="Sarah"
print(myPerson.name.firstname)
print(myPerson1.name.firstname)

