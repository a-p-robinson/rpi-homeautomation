#!/bin/python

from gpiozero import Energenie

lamp = Energenie(1)
lamp.off()
