import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
timestamp=time.strftime("%H")
print(timestamp)
timestamp=time.strftime("%M")
print(timestamp)
timestamp=time.strftime("%S")
print(timestamp)
import time
# hour=input("Enter the hour First:")
hour=time.strftime("%H")
hour = int(hour)
if(hour>=0 and hour<=17):
    print("Good Morning")
elif(hour>=17 and hour<=22):
    print("Good AfterNoon")
else:
    print("Good Night")