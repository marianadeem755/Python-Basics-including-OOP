class Employee:
    Company_Name="Apple"
    No_of_employees=100
    def __init__(self, name, id):
        self.name=name
        self.id=id 
        self.raise_amount=0.02
        self.No_of_employees=100
    def show(self):
        print(f"This is the best employee {self.name} in the company and has id is {self.id} and it has raise amount is {self.raise_amount} and is the proficient employee in {self.Company_Name}. The No of Employees in the company is {self.No_of_employees}")
emp1=Employee("Maria Nadeem", "1")
print(emp1.name, emp1.id)
emp1.raise_amount= 0.5
# emp1.Company_Name="Tesla"
Employee.Company_Name="Tesla"
emp1.show()
print(emp1.Company_Name)
emp2=Employee("Shazia Nadeem", "5")
print(emp2.name, emp2.id)
emp2.show()
# Employee.show(emp1)


        