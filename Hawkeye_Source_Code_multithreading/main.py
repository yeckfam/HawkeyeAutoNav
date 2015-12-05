__author__ = 'tianlan'

import time
import initialization
import operations
import cleanup
import atexit
import command_thread
import range_sensor_thread
import configuration
from multiprocessing import Process, Manager

runtime = configuration.config['runtime']

atexit.register(cleanup.cleanup())

def timeout(to):
    time.sleep(to)

def main ():
    loop = 0
    manager = Manager()
    distance = manager.list([0, 0, 0, 0, 0, 0])
#    distance2 = manager.list([0, 0, 0, 0, 0, 0])
    #Step 1: Initialzation
    initialization.initialize()
    #Step 2: Departure
    operations.take_off()
    #Step 3: Multi threading start
    timeout_thread = Process(target = timeout, args = (runtime, ))
    p1 = Process(target = command_thread.command_thread_wrapper_function, args = (distance, ))
    p2 = Process(target = range_sensor_thread.range_sensor_wrapper_function, args = (distance, ))
    p1.start()
    p2.start()
    timeout_thread.start()
    #Step 4: Multi threading end
    timeout_thread.join()
    p1.terminate()
    p2.terminate()
    time.sleep(1)
    cleanup.cleanup()

main()
