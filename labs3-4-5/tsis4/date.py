# ex1
from datetime import datetime, timedelta

tday = datetime.now()
fivedays = tday - timedelta(days=5)
print("Five days ago was =", fivedays)



# ex2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday was =", yesterday)
print("Today is =", today)
print("Tomorrow will be =", tomorrow)



# ex3
dtime = datetime.now()
dtime_mic = dtime.replace(microsecond=0)
print("datetime without microseconds =", dtime_mic)



# ex4
date1 = datetime(2024, 3, 20, 12, 0, 0)
date2 = datetime(2024, 3, 21, 12, 0, 0)

diff = date2 - date1
diffsec = diff.total_seconds()
print("Difference in seconds:", diffsec)