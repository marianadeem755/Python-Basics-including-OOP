# f=open("code_with_herry_course/file.txt","r")
# i=0
# while True:
#     i=i+1
#     lines=f.readline()
#     if not lines:
#         break
#     m1=int(lines.split(",")[0])
#     m2=int(lines.split(",")[1])
#     m3=int(lines.split(",")[2])
#     m4=int(lines.split(",")[3])
#     m5=int(lines.split(",")[4])
#     print(f"The marks of student {i} is: {m1*2}")
#     print(f"The marks of student {i} is: {m2*2}")
#     print(f"The marks of student {i} is: {m3*2}")
#     print(f"The marks of student {i} is: {m4*2}")
#     print(f"The marks of student {i} is: {m5*2}")

# write function
f=open("code_with_herry_course/file1.txt", "w")
lines=("My name is\n", "Maria Nadeem\n", "I've recently completed my bachelors in chemistry")
f.writelines(lines)



    




