time=int(input("Hey! Can you please tell what's the time now in your country:"))
if time == 8:
    print("Hello! Good Afternoon!")
elif time==12:
    print("Hello! Good Morning")
elif time==4 or time == 5:
    print("Hello! Good evening")
else:
    print("Good Night! Have sweet Dreams")
import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
Hour=time.strftime("%H")
print(Hour)
sec=time.strftime("%S")
print(sec)

