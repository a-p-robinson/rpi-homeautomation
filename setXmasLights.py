#!/usr/bin/python

import datetime
from crontab import CronTab
from astral import Astral
from random import randint

# Return a list of dates between strat and end
def datetime_range(start=None, end=None):
    span = end - start
    for i in xrange(span.days + 1):
        yield start + datetime.timedelta(days=i)

# Start the day we run the script
now = datetime.datetime.now()
start = datetime.date(now.year,now.month,now.day)
# End on 12th night (5th)
end = datetime.date((now.year +1),1,05)

print 'Starting on ' , start
print 'Endin on    ' , end

offTimePM = datetime.time(23,59)
offTimeWE = datetime.time(23,59)

cron  = CronTab(user=True)

city_name = 'Manchester'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]

for date in datetime_range(start, end):

    on_jobAM  = cron.new(command='/root/homeAutomation/on.py 3 >> /var/log/cron/lights_xmas.log')
    off_jobAM = cron.new(command='/root/homeAutomation/off.py 3  >> /var/log/cron/lights_xmas.log')
    on_jobPM  = cron.new(command='/root/homeAutomation/on.py 3 >> /var/log/cron/lights_xmas.log')
    off_jobPM = cron.new(command='/root/homeAutomation/off.py 3 >> /var/log/cron/lights_xmas.log')
    
    print date

    # Find the sunrise and sunset time
    sun = city.sun(date=date, local=True)

    for j in [on_jobAM, off_jobAM, on_jobPM, off_jobPM]:
        j.day.on(date.day)
        j.month.on(date.month)
    
    # Check if date is a weekend
    if date.weekday() < 5:
        on_jobAM.hour.on(sun['dawn'].hour)
        on_jobAM.minute.on(sun['dawn'].minute - 2)
        off_jobAM.hour.on(sun['dawn'].hour + 2)
        off_jobAM.minute.on(sun['dawn'].minute - 2)
       
        on_jobPM.hour.on(sun['sunset'].hour)
        on_jobPM.minute.on(sun['sunset'].minute - 2)
        off_jobPM.hour.on(offTimePM.hour)
        off_jobPM.minute.on(offTimePM.minute - randint(0,15))

    else:
        print " WEEKEND:"
        on_jobAM.hour.on(sun['dawn'].hour + 3)
        on_jobAM.minute.on(sun['dawn'].minute - 2)
        off_jobPM.hour.on(offTimeWE.hour)
        off_jobPM.minute.on(offTimeWE.minute - randint(0,15))

        # Delete the other two jobs
        cron.remove(off_jobAM)
        cron.remove(on_jobPM)

for job in cron:
    print job

cron.write()

