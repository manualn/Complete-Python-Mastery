class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(Self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor")
        self.weight = 2
        super().__init__()


m = Mammal()
print(m.age)
print(m.weight)