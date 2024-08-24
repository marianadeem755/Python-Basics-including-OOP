class parent_class:
    def parent_method(self):
        print("This is the parent class1")
class child_class(parent_class):
    def parent_method(self):
        print("Maria")
        super().parent_method()
    def child_method(self):
        print("This is the child method2")
        super().parent_method()
obj=child_class()
# obj.child_method()
obj.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id
class programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang=lang
a=Employee("Maria", 3456)
print(a.name, a.id)
b=programmer("Maria Nadeem", 786, "python") 
print(b.name, b.id, b.lang)   

class parent_class:
    def parent_method(self):
        print("This is the parent method")
class child_class(parent_class):
    def parent_method(self):
        print("Maria")
        super().parent_method()
    def child_method(self):
        print("This is the child method")
        super().parent_method()
obj=child_class()
# obj.child_method()
obj.parent_method()