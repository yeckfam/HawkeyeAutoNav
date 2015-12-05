__author__ = 'tianlan'

import range_sensor
import operations
import range_sensor_thread
import command_thread
import time

def cleanup() :
    time.sleep(1)
    range_sensor.range_sensor_cleanup()
    operations.operations_cleanup()
