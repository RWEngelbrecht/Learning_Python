## static and class methods

class Person(object):
    # variable that belongs to class
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod # decorator
    def getPopulation(cls): # method belonging to the class, not an instance
        return cls.population

    @staticmethod 
    def isPerson(obj):
        return isinstance(obj, Person)

    def isAdult(self):
        return self.age >= 18

    def display(self):
        print(self.name, "is",self.age,"years old", sep=' ')

per1 = Person("Steve", 18)
per1.display()
print(Person.getPopulation())
print("Yep, that's a person...") if Person.isPerson(per1) else print("That's no human...")