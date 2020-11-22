######################################
# Inheritance - is-a relationship
# use this to have an implied feature in base classes
# !!!AVOID MULTIPLE INHERITANCE IF YOU CAN!!!
# use inheritance only when there are clearly related reusable pieces of code that fit under a common concept or if you have to
######################################

class Parent():

    def override(self):
        print("PARENT override")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

################################################
# Composition - has-a relationship
# gives you modules and capability to call functions in other classes
# use to package code into modules that are used in many unrelated places and situations
################################################

class Other():

    def override(self):
        print("OTHER override")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Kid(Other):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Kid override()")

    def altered(self):
        print("Kid, BEFORE OTHER altered()")
        super(Kid, self).altered()
        print("Kid, AFTER OTHER altered()")

daughter = Kid()

daughter.implicit()
daughter.override()
daughter.altered()