class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()

class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass