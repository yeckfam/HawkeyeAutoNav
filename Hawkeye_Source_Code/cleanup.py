_author__ = 'tianlan'

import range_sensor
import operations

def cleanup() :
    range_sensor.range_sensor_cleanup()
    operations.operations_cleanup()
