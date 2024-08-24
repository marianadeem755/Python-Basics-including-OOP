# Multilevel Inheritance in Python
# Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits 
# from another derived class. This type of inheritance allows you to build a hierarchy of classes
#  where one class builds upon another, leading to a more specialized class.

# In Python, multilevel inheritance is achieved by using the class hierarchy.
#  The syntax for multilevel inheritance is quite simple and follows the same syntax as single inheritance.

# Syntax
# class BaseClass:
#     # Base class code
    
# class DerivedClass1(BaseClass):
#     # Derived class 1 code
    
# class DerivedClass2(DerivedClass1):
#     # Derived class 2 code
# In the above example, we have three classes: BaseClass, DerivedClass1, and DerivedClass2.
#  The DerivedClass1 class inherits from the BaseClass, and the DerivedClass2 class inherits
#  from the DerivedClass1 class. This creates a hierarchy where DerivedClass2 has access to all 
# the attributes and methods of both DerivedClass1 and BaseClass.

# Example
# Let's take a look at an example to understand how multilevel inheritance works in Python. Consider the following classes:

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")
# In this example, we have three classes: Animal, Dog, and GoldenRetriever. 
# The Dog class inherits from the Animal class, and the GoldenRetriever class inherits from the Dog class.

# Now, when we create an object of the GoldenRetriever class, it has access to all the attributes 
# and methods of the Animal class and the Dog class. We can also see that the GoldenRetriever class has its own
#  attributes and methods that are specific to the class.

# dog = GoldenRetriever("Max", "Golden")
# dog.show_details()
# Output:
# Name: Max
# Species: Dog
# Breed: Golden Retriever
# Color: Golden
# As we can see from the output, the GoldenRetriever object has access to all the attributes and methods of the Animal and Dog classes, and, it has also added its own unique attributes and methods. This is a powerful feature of multilevel inheritance, as it allows you to create more complex and intricate classes by building upon existing ones.

# Another important aspect of multilevel inheritance is that it allows you to reuse code and avoid repeating the same logic multiple times. This can lead to better maintainability and readability of your code, as you can abstract away complex logic into base classes and build upon them.

# In conclusion, multilevel inheritance is a powerful feature in object-oriented programming that allows you to create complex and intricate classes by building upon existing ones. It provides the benefits of code reuse, maintainability, and readability, while also requiring careful consideration to avoid potential problems.

class Animal:
    def __init__(self, name, specie):
        self.name=name
        self.specie=specie
    def show_details(self):
        print(f"The name of the Animal is {self.name} and specie is {self.specie}")
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, specie="Asian cat")
        self.breed=breed
    def show_details(self):
        Animal.show_details(self)
        print(f"The Breed of Animal is {self.breed}")
        print(f"The name of the Animal is {self.name} and the specie is {self.specie}")
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color=color
    def show_details(self):
        Dog.show_details(self)
        print(f"The color of Animal is {self.color}")
        print(f"The name of the animal is {self.name} and its color is {self.color}")
o=GoldenRetriever("Cat", "white")
o.show_details()
print(o.name,o.specie,o.breed,o.color)
