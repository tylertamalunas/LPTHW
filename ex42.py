## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??  Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##?? Dog has-a name
        self.name = name

## ?? Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##?? Cat has-a name
        self.name = name

##?? Person is-a object
class Person(object):

    def __init__(self, name):
        ##?? People has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None


##?? Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##?? employee has a name and salary
        super(Employee, self).__init__(name)
        ##?? employee has a salary
        self.salary = salary

##?? fish is-a object
class Fish(object):
    pass

##?? salmon is-a fish
class Salmon(Fish):
    pass

##?? halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a dog
rover = Dog("Rover")

##?? satan is-a cat
satan = Cat("Satan")

##?? mary is-a person
mary = Person("Mary")

##?? mary has-a pet satan
mary.pet = satan

##?? frank has-a salary of 120000
frank = Employee("Frank", 120000)

##?? frank has-a pet rover
frank.pet = rover

##?? flipper is-a fish
flipper = Fish()

##?? crouse is-a salmon
crouse = Salmon()

##?? harry is-a halibut
harry = Halibut()