import time
timestamp = time.strftime('%H:%M:%S')

hour = int(time.strftime('%H'))
print(hour)

if(hour >= 0 and hour < 12):
    print("Good Morning sir")
elif(hour >= 12 and hour < 15):
    print("Good Afternoon sir")
elif(hour >= 15 and hour < 17):
    print("Good Evening sir")
if(hour >= 17 and hour <= 24):
    print("Good Night sir")

    