__author__ = 'tianlan'

import operations
import time
import configuration

def command_thread_wrapper_function (distance):
    while True:
        # Step 1: Get range
        for i in range (0, configuration.config['num_directions']):
            print "Command_Thread::::Tian:: i = ", i, "distance[i] = ", distance[i]
        # Step 2: Come up with commands
        # Step 3: Issue commands
        operations.hover()
