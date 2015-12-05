__author__ = 'tianlan'

import time
import initialization
import operations
import cleanup
import atexit
import command_thread
import range_sensor_thread
import configuration
import keyboard_thread
import goback_thread

from multiprocessing import Process, Manager

runtime = configuration.config['runtime']

atexit.register(cleanup.cleanup())

def timeout(to):
    time.sleep(to)

def main ():
    manager = Manager()

    # Range Sensor Distance
    distance = manager.list([0, 0, 0, 0, 0, 0])

    # DataBase
    db = manager.list()

    # Command from Keyboard
    keyboard_cmd = manager.dict()
    keyboard_cmd['vld'] = 0
    keyboard_cmd['cmd'] = ''

    # GoBack Ready
    goback_cmd = manager.dict()
    goback_cmd['vld'] = 0

    #Step 1: Initialzation
    initialization.initialize()
    #Step 2: Departure
    operations.take_off()
    #Step 3: Multi threading start
    to_thr = Process(target = timeout, args = (runtime, ))
    key_thr = Process(target = keyboard_thread.keyboard_thread_wrapper_function, args = (keyboard_cmd, ))
    cmd_thr = Process(target = command_thread.command_thread_wrapper_function, args = (distance, keyboard_cmd, db, goback_cmd, ))
    rs_thr = Process(target = range_sensor_thread.range_sensor_wrapper_function, args = (distance, ))
    gb_thr = Process(target = goback_thread.goback_wrapper_function, args = (goback_cmd, ))

    cmd_thr.start()
    rs_thr.start()
    to_thr.start()
    key_thr.start()
    gb_thr.start()

    #Step 4: Multi threading end
    to_thr.join()
    cmd_thr.terminate()
    rs_thr.terminate()
    key_thr.terminate()
    gb_thr.terminate()

    operations.landing()

    time.sleep(1)
    cleanup.cleanup()

main()
