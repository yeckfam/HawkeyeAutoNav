#!/bin/bash

echo "Front:"
sudo python range_sensor1.py
sleep 2
echo "Back:"
sudo python range_sensor2.py
sleep 2
echo "Left:"
sudo python range_sensor3.py
sleep 2
echo "Right:"
sudo python range_sensor4.py
sleep 2
echo "Bottom:"
sudo python range_sensor5.py
sleep 2
echo "Top:"
sudo python range_sensor6.py
