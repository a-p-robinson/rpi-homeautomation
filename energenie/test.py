#!/bin/python

from gpiozero import Energenie

lamp = Energenie(2)
lamp.on()

print("Lamp is {}".format(lamp.socket))
