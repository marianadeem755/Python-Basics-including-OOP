# Multiple Inheritance in Python
# Multiple inheritance is a powerful feature in object-oriented programming that allows a class 
# to inherit attributes and methods from multiple parent classes. 
# This can be useful in situations where a class needs to inherit functionality from multiple sources.

# Syntax
# In Python, multiple inheritance is implemented by specifying multiple parent classes 
# in the class definition, separated by commas.

# class ChildClass(ParentClass1, ParentClass2, ParentClass3):
#     # class body
# In this example, the ChildClass inherits attributes and methods from all three parent classes:
#  ParentClass1, ParentClass2, and ParentClass3.

# It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO)
#  to resolve conflicts between methods or attributes from different parent classes. 
# The MRO determines the order in which parent classes are searched for attributes and methods.
class Employee:
    def __init__(self, name):
        self.name=name
    def show(self):
        print(f"The name of the employee is {self.name}")
class Dancer:
    def __init__(self, Dance):
        self.Dance=Dance
    def show(self):
        print(f"She can performs {self.Dance} Dance")
class DancerEmployee(Employee, Dancer):
    def __init__(self, name, Dance):
        self.name=name
        self.Dance=Dance
o=DancerEmployee("Nitika", "Khatak")
print(o.name, o.Dance)
o.show()
print(DancerEmployee.mro())

class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species
    def show(self):
        print(f"The name of the mammal is {self.name} and specie is {self.species}")
class Mammal:
    def __init__(self, fur_color, routine):
        self.fur_color=fur_color
        self.routine=routine
    def show(self):
        print(f"The fur color of the mammal is {self.fur_color} and routine is {self.routine}")
class MammalianAnimal(Mammal, Animal):
    def __init__(self, name, species, fur_color, routine, breed):
       self.name=name
       self.species=species
       self.fur_color=fur_color
       self.routine=routine
       self.breed=breed
m=MammalianAnimal("cats", "domestic cat", "red", "flying", "Meat")
print(m.name, m.species, m.fur_color, m.routine, m.breed)
m.show()

        
        


        
        




        
        
    