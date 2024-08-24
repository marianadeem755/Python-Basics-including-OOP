class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Hey this is the Dog!")
class Dog(Animal):
    def __init__(self, name, specie="Dog"):
        print(f"The name of animal is {name} and specie is {specie}")
    def make_sound(self):
        print("Bark!")
a=Animal("Dog", "Doggerman")
print(a.name, a.species)
a.make_sound()
b=Dog("Dog", "pet")
b.make_sound()
        
class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species
    def eat(self):
        print("Hey this is the Cat!")
class Cat(Animal):
    def __init__(self, name, specie="Cat"):
        print(f"The name of animal is {name} and specie is {specie}")
    def eat(self):
        print("Eat Meat")
a=Animal("Cat", "Catcare")
print(a.name, a.species)
a.eat()
b=Cat("Cat", "pet")
b.eat()