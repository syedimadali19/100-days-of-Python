#Program to greet the user based on the system time
import time
name=input("Enter your name:").title()
timestamp=time.strftime('%H:%M:%S')
print("Time:",timestamp)

hour=int(time.strftime('%H'))
if(hour>=5 and hour<12):
    print("Good Morning",name)
elif(hour>=12 and hour<18):
    print("Good Afternoon",name)
else:
    print("Good Evening",name)

print("Hope you have a nice day")