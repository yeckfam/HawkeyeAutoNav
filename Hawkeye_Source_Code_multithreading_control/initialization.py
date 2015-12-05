__author__ = 'tianlan'

import time
import range_sensor
import configuration

setup_time = configuration.config['setup_time']

def initialize ():
    range_sensor.range_sensor_init()
    time.sleep(setup_time)

