string="Firstly, tell me what is your name: Hy! My name  is {1} and I completed my graduation in {0}"
name="Maria Nadeem"
subject="Bs.chemistry"
print(string.format(subject,name))

name="Maria Nadeem"
country="Pakistan"
print(f"My Name is {name} and I lives in {country}")

value_number="The number which i obtained in matric Exams are:\n {:.2f}"
number=1027.876540012
print(value_number.format(number))

print(f"The value number is:\n{number:.2f}")

info="My Name is {} and I'm from{}"
name="Maria Nadeem"
country ="Pakistan"
print(info.format(name, country))
print(f"My name is {name} and I lives in {country}")

score="what your score now {:.2f}"
score=67.0009087
print("My score in the written test is:{score}")

print(f"My score in the written test is: {score:.2f}")

hobby="My hobby is {}"
hob="study and coding"
print(hobby.format(hob))

print(f"My hobby is {hob}")
print(f"The f steing also written as: {{hob}}") # when we have to take the brackets around any word then we add the double brackets

print(f"The number is:{2*57}")