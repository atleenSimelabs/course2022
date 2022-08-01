class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

mrbrun=Person("Mr. Burdell",53)
mrsbrun=Person("Mrs. Burdell", 53)
george_p=Person("George P. Burdell",25, mrbrun, mrsbrun)

print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)


