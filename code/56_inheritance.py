class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")



class Mammal(Animal):
    #def eat(self):
    #    print("eat")

    def walk(self):
        print("walk")


class Fish(Animal):
    #def eat(self):
    #    print("eat")

    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)
