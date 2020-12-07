#!/bin/python

import sys
from gpiozero import Energenie

number = int(sys.argv[1])

print('Turning switch {} off.'.format(number))

a = Energenie(number)
a.off()

