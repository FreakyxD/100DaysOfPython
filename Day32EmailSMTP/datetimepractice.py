import datetime as dt
import time

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
#print(type(now))

if year == 2020:
    print("Pandemic ongoing")

# creating own dt object
date_of_birth = dt.datetime(year=2000, month=12, day=1)
print(date_of_birth)


# x = 0
# while x < 1000000324324:
#     time.sleep(1)
#     now = dt.datetime.now()
#     print(now)
#     x += 1
