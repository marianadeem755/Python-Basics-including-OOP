# Exercise 11 - Drink Water Reminder
# Write a python program which reminds you of drinking water every hour or two.
#  Your program can either beep or send desktop notifications for a specific operating system
from plyer import notification
from PIL import Image
import time
filename="code_with_herry_course/daniel-sinoca-JsDoC8BJCcI-unsplash.jpg"
img=Image.open(filename, "r")
img.save("code_with_herry_course/daniel-sinoca-JsDoC8BJCcI-unsplash.ico")
uset_input= int(input("Hi programmer, By How many hours you are working: "))
if uset_input>=1:
    notification.notify(title = "Watering Remainder",
    message="Hey Programmer!There is about more than hour to work, Now it time to drink water" ,
    app_icon = "code_with_herry_course/daniel-sinoca-JsDoC8BJCcI-unsplash.ico",
           
    # displaying time
    timeout=2)
else:
    pass

import os

# filename = "code_with_herry_course/daniel-sinoca-JsDoC8BJCcI-unsplash.ico"

# # Check if the file exists
# if os.path.exists(filename):
#     print("The file exists.")
# else:
#     print("The file does not exist.")




