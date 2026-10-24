import time
user_time_set = int(input("Enter the time in seconds: "))

for i in range(user_time_set, 0, -1):
    second = i % 60
    minute = i // 60
    hour = i //3600
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("Hey,time's up!")
