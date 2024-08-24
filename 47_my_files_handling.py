# There are various modes in which we can open files.

# `read (r):`` This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

# `write (w):`` This mode opens the file for writing only and creates a new file if the file does not exist.

# `append (a):` This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.

# `text (t):` Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

# `binary (b):` used to handle binary files (images, pdfs, etc)# f=open("code_with_herry_course/48_my_file.txt", "r")

# `Reading from a File`
# Once we have a file object, we can use various methods to read from the file.

# The read() method reads the entire contents of the file and returns it as a string.

# Writing to a File
# To write to a file, we first need to open it in write mode.
# We can then use the write() method to write to the file.
# Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.

# Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.
# The 'with' statement
# Alternatively, you can use the with statement to automatically
#  close the file after you are done with it.
f=open("code_with_herry_course/48_my_file.txt","r")
text=f.read()
print(text)
f.close()

f=open("code_with_herry_course/48_my_file.txt", "w")
text=f.write("Hey how are you I'm well what are you doing these days?")
print(text)
f.close()

f=open("code_with_herry_course/48_my_file.txt", "a")
text=f.write("Nice to meet you: Same Here")
print(text)
f.close()

with open("code_with_herry_course/48_my_file.txt", "a") as f:
    f.write("I'm Maria Nadeem Currently completed my bachelors in chemistry")