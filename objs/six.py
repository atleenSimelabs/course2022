class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def capitalizename(name):
    name.firstname=name.firstname.upper()
    name.lastname=name.lastname.upper()

myPerson = Person(Name("David", "Joyner"), "brown", 30)
capitalizename(myPerson.name)
print(myPerson.name.firstname)
print(myPerson.name.lastname)
print(myPerson.eyecolor)
print(myPerson.age)

