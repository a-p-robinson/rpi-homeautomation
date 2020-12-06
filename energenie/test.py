#!/bin/python

from gpiozero import Energenie

lamp = Energenie(2)
lamp.off()

print("Lamp is {}".format(lamp.socket))
