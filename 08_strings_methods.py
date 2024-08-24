# upper case
a="Hy, It's Maria Nadeem"
print(a.upper())
#Lower case
print(a.lower())
# split (it splits and returns the output as  the list)
b="Maria Nadeem"
print(b.split())
# strip (Removes white space before and after string)
c=" Maria Nadeem    "
print(c.strip())
# rstrip (Removes the trailing characters)
d="Heloo It's Me!!!!"
print(d.rstrip("!"))
# capitalize (# It capitalize the First word of sentence)
e="hi,how are you \n does you try to teach python"
print(e.capitalize())
#title
f="world health organization"
print(f.title())
#replace (It replace the given word with the provided word and used only single bracket for replacining that with this not with in two brackets)
g="Maria Azhar Khan"
print(g.replace("Maria" , "Nadeem"))
# center
f="My name is Maria Nadeem"
print(f.center(50))
print(f.center(50, "."))
# endswith
m="she is Shazia Nadeem!!!"
print(m.endswith("!"))
n="!!!she is Shazia Nadeem"
print(n.startswith("!"))
r="what's your job now in this company"
print(r.find("your"))
print(r.find("Maria"))
# isalnum #we have to write it without any space and it finds a-z,A-Z,0-9
q="Areyoulearningpython009course"
print(q.isalnum())
# isalpha
p="Mynameismarianadeem" #we have to write it without any space and it finds a-z,A-Z
print(p.isalpha())
i="mynameismariandeem755"
print(i.isalpha())
mn="My Name is Maria Nadeem"
print(mn.upper())
nm="My Name is Maria Nadeem"
print(nm.lower())
er="my name is marianadeem"
print(er.count('m'))
print(er.isprintable())
org="     " # not giving any character in it so that it detects that the space is present
print(org.isspace())
wr="World Health Organization"
print(wr.istitle())
