#!/bin/python

from gpiozero import Energenie

lamp = Energenie(4)
lamp.off()

print("Lamp is {}".format(lamp.socket))
