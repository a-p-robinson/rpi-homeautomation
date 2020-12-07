#!/bin/bash

#set -e
source /home/apr/rpi-homeautomation/energenie/env/bin/activate

## DO SOME STUFF -> USE FULL PATH HERE TOO #
python /home/apr/rpi-homeautomation/energenie/switch_on.py $1 > /home/apr/rpi-homeautomation/energenie/log.log

deactivate

