#!/bin/bash

#set -e
source /home/apr/rpi-homeautomation/energenie/env/bin/activate

## DO SOME STUFF -> USE FULL PATH HERE TOO #
python /home/apr/rpi-homeautomation/energenie/switch_off.py 4 > /home/apr/rpi-homeautomation/energenie/log.log

deactivate

