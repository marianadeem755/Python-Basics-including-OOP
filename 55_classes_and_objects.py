class person:
    name="Maria Nadeem"
    occupation="Datascience"
    study="BS Chemistry"
    Hobby="Study and Coding"
    # define method
    def info(self):
        print(f"{self.name} is {self.occupation} and doing {self.study}, {a.Hobby}")
a=person()
b=person()
c=person()
a.name="Shazia Nadeem"
a.occupation="House wife"
a.study="Lotus Degree"
a.Hobby="All works of Home"
b.name="Nadeem Azhar Khan"
b.occupation="Business man"
b.study="FSC"
b.Hobby="work on shop"

print(a.name, a.occupation, a.study, a.Hobby)
a.info()
print(b.name, b.occupation, b.study, b.Hobby)
b.info()
c.info()
