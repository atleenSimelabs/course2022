class Person:
    def __init__(self, name, eyecolor, age):
        self.name=name
        self.eyecolor=eyecolor
        self.age=age

class Name:
    def __init__(self, firtsname, lastname):
        self.firstname=firtsname
        self.lastname=lastname

myPerson=Person(Name("Atleen", "Jose"), "brown", 30)
print(myPerson.name.firstname)
print(myPerson.name.lastname)
print(myPerson.eyecolor)
print(myPerson.age)
        
        
        