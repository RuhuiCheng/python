from datetime import datetime

dt_now = int(datetime.now().timestamp())
dt_before = 1552754065

minutes = (dt_now - dt_before)/60

print(minutes)