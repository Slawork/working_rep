from datetime import datetime

now = datetime.now()
formatted_now = now.strftime('%H:%M')
total_minutes = now.hour * 60 + now.minute
schedule = list(range(420,1380+1,20))
bus_time = 420
stop_bus_time = 1380
target = total_minutes + 5
if target > 1380:
    if total_minutes <= 420:
            wait = (420 - 5) - total_minutes
            print(wait, 0)
    else:
            wait = (1440 - total_minutes) + (420 - 5)
            print(wait)
else:
    for bus_time in schedule:
        if bus_time >= target:
            exit_time = bus_time - 5
            wait = exit_time - total_minutes
            print(wait)
            break
    else:
        print("Автобусов больше нет")

