#!/usr/bin/python

import sys
import time
from energenie import switch_on
from energenie import switch_off

switch = int(sys.argv[1])

print 'Assocating switch with number ', switch
switch_on(switch)
time.sleep(10)
switch_off(switch)
print 'Associated with number 1'
