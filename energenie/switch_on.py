#!/bin/python

import sys
from gpiozero import Energenie

number = int(sys.argv[1])

print('Turning switch {} on.'.format(number))

switch = Energenie(number)
switch.off()



#print("Lamp is {}".format(lamp.socket))
