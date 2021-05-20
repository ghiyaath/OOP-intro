from datetime import date
d = date (2021, 5, 18,)
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%y %m %d"))

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)



