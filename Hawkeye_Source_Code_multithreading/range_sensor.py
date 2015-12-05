__author__ = 'tianlan'

import RPi.GPIO as GPIO
import time
import configuration

GPIO.setmode(GPIO.BCM)

directions = configuration.config['directions']

TRIG = configuration.config['TRIG']
ECHO = configuration.config['ECHO']
num_directions = configuration.config['num_directions']

def range_sensor_init ():
    for i in range (0, num_directions):
        GPIO.setup(TRIG[i], GPIO.OUT)
        GPIO.output(TRIG[i], False)
    for i in range (0, num_directions):
        GPIO.setup(ECHO[i], GPIO.IN)
    #time.sleep is put in initialization.py

def detect_range (direction):
    trig = TRIG[direction]
    echo = ECHO[direction]
    pulse_start = time.time()
    pulse_end = 0
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    while GPIO.input(echo)==0:
        pulse_start = time.time()
    while GPIO.input(echo)==1:
        pulse_end = time.time()
    print "%d, %d" % (pulse_end, pulse_start)
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print "Direction:",direction,"Distance:",distance,"cm"
    return distance
    #time.sleep is put in main.py

def range_sensor_cleanup():
    GPIO.cleanup()
