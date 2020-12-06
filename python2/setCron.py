#!/bin/python


import datetime
from crontab import CronTab
from astral import Astral
from random import randint

# Return a list of dates between strat and end
def datetime_range(start=None, end=None):
    span = end - start
    for i in xrange(span.days + 1):
        yield start + datetime.timedelta(days=i)

start = datetime.date(2016,1,01)
end = datetime.date(2016,1,03)

offTimePM = datetime.time(23,59)
offTimeWE = datetime.time(23,59)

cron  = CronTab(user=True)

city_name = 'Manchester'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]

for date in datetime_range(start, end):

    on_jobAM  = cron.new(command='python /home/apr/homeAutomation/src/on1.py  > /var/log/cron/lights_stand.log')
    off_jobAM = cron.new(command='python /home/apr/homeAutomation/src/off1.py  > /var/log/cron/lights_stand.log')
    on_jobPM  = cron.new(command='python /home/apr/homeAutomation/src/on1.py  > /var/log/cron/lights_stand.log')
    off_jobPM = cron.new(command='python /home/apr/homeAutomation/src/off1.py  > /var/log/cron/lights_stand.log')
    
    print date.strftime("%m %d")

    # Find the sunrise and sunset time
    sun = city.sun(date=date, local=True)

    for j in [on_jobAM, off_jobAM, on_jobPM, off_jobPM]:
        j.day.on(date.day)
        j.month.on(date.month)
    
    # Check if date is a weekend
    if date.weekday() < 5:
        on_jobAM.hour.on(sun['dawn'].hour)
        on_jobAM.minute.on(sun['dawn'].minute)
        off_jobAM.hour.on(sun['dawn'].hour + 2)
        off_jobAM.minute.on(sun['dawn'].minute)
       
        on_jobPM.hour.on(sun['sunset'].hour)
        on_jobPM.minute.on(sun['sunset'].minute)
        off_jobPM.hour.on(offTimePM.hour)
        off_jobPM.minute.on(offTimePM.minute - randint(0,15))

    else:
        print " WEEKEND:"
        on_jobAM.hour.on(sun['dawn'].hour + 3)
        on_jobAM.minute.on(sun['dawn'].minute)
        off_jobPM.hour.on(offTimeWE.hour)
        off_jobPM.minute.on(offTimeWE.minute  - randint(0,15))

        # Delete the other two jobs
        cron.remove(off_jobAM)
        cron.remove(on_jobPM)

for job in cron:
    print job

cron.write()

