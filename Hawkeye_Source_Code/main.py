__author__ = 'tianlan'

import time

import initialization
import range_sensor
import operations
import cleanup
import atexit

atexit.register(cleanup.cleanup())

distance = [0, 0, 0, 0, 0, 0]

hover_thr = 1500

def main ():
    loop = 0
    #Step 1: Initialzation
    initialization.initialize()
    #Step 2: Departure
    operations.take_off()
    #while True :
    while (loop < 300): #time for a loop: 0.15s
        loop += 1
        #Step 2: Detect Range
#        for i in range(0, range_sensor.num_directions):
#            distance[i] = range_sensor.detect_range(i)
        distance[4] = range_sensor.detect_range(4)
        time.sleep(0.05)
        #Step 3: Analyze Range
#        if (distance[4] > 180):
#            #operations.hover()
#            operations.move_backward()
#        elif (distance[4] < 180):
#            #operations.hover()
#            operations.move_backward()
#        else:
#            #operations.hover()
#            operations.move_backward()
        #Step 4: Generate Next Command
        if (loop < 50):
            operations.hover()
        elif (loop < 100):
            operations.move_backward()
        elif (loop < 150):
            operations.hover()
        elif (loop < 200):
            operations.move_backward()
        elif (loop < 250):
            operations.drop()
        else :
            operations.drop()
    cleanup.cleanup()

main()
