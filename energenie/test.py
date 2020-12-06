#!/bin/python

from gpiozero import Energenie

lamp = Energenie(1)
lamp.on()

print("Lamp is {}".format(lamp.socket))
