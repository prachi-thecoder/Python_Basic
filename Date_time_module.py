import datetime as dt
# get the current date and time
# now = dt.datetime.now()
# print(now)

# get current date
current_date = dt.date.today()
print(current_date)
print("current year:",current_date.year)
print("current month:",current_date.month)
print("current day:",current_date.day)

# get custom date
d = dt.date(2024,12,25)
print(d)

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time (hour , min, sec , microsecond)
c = time(11,24,44,335686)
print(c)

from datetime import datetime,timedelta
# datetime (year , month , day)
a= datetime(2025,12,28)
print(a)

# datetime (year,month, day,hour ,min, sec, micro sec)
b= datetime(2022,12,24,23,55,59,68746)
print(b)

# to find the difference bet date year
from datetime import datetime,timedelta
# datetime (year , month , day)
a= datetime(2022,12,28)
print(a)
b= datetime(2025,12,3)
print(b)
print(b-a)

import datetime as dt
d = dt.date(2024,12,25)
print(d)
k=dt.date(2022,11,2)
print(k)
print(d-k)

#take from user date
from datetime import datetime
d=input("enter a date:")
print(d.split("/"))
m=input("enter a month:")
print(m.split("/"))
y=input("enter a year:")
print(y.split("/"))
# datetime(y,m,d)
print(datetime(int(y),int(m),int(d)))

