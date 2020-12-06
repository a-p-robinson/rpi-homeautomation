#!/bin/bash

# Check if the install directory exists and make it if it doesn't
if [ ! -d "/opt/ha-bridge" ]; then
  sudo mkdir /opt/ha-bridge
fi

# Download the java file
vers="5.3.0"

cd /opt/ha-bridge
sudo wget https://github.com/bwssytems/ha-bridge/releases/download/v$vers/ha-bridge-$vers.jar

