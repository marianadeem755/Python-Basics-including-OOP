f=open("code_with_herry_course/file.txt", "r")
lines=f.seek(15)
print(lines)
lines=f.read(10) # The 10 byte include read new line character
print(lines)
lines=f.tell()
print(lines)
with open("code_with_herry_course/sample_file_1.txt","w") as f:
    f.write("My name is\n Maria Nadeem\n I've recently completed my bachelors in chemistry")
    f.truncate(45)

 

