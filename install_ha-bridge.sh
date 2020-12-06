#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if the install directory exists and make it if it doesn't
if [ ! -d "/opt/ha-bridge" ]; then
  sudo mkdir /opt/ha-bridge
fi

# Download the java file
vers="5.3.0"

cd /opt/ha-bridge
sudo wget https://github.com/bwssytems/ha-bridge/releases/download/v$vers/ha-bridge-$vers.jar

mv ha-bridge-$vers.jar ha-bridge.jar

# Install the systemd service
sudo cp $DIR/config/ha-bridge.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start ha-bridge.service
sudo systemctl enable ha-bridge.service
