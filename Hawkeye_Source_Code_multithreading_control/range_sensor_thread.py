__author__ = 'tianlan'

import range_sensor
import time
import configuration

num_directions = configuration.config['num_directions']
range_sensor_detect_gap = configuration.config['range_sensor_detect_gap']

def range_sensor_wrapper_function(distance):
    while True:
#        for i in range(0, num_directions):
#        for i in range(0, 1):
#            distance[i] = range_sensor.detect_range(i)
#            print "Range_Sensor_Thread::::Tian:: i = ", i, "distance[i] = ", distance[i]
        time.sleep(range_sensor_detect_gap)
