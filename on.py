#!/usr/bin/python

import sys
import time

from energenie import switch_on
from energenie import switch_off

switch = int(sys.argv[1])

print time.ctime(time.time())
print 'Switching ON number ', switch
switch_on(switch)
time.sleep(5)
switch_on(switch)
time.sleep(5)
switch_on(switch)
time.sleep(5)
switch_on(switch)

