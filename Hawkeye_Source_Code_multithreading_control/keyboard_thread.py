__author__ = 'tianlan'

import getch
import time

def keyboard_thread_wrapper_function(keyboard_cmd):
    while True:
        char = getch.getch()
        print 'char = ', char
        keyboard_cmd['cmd'] = char
        keyboard_cmd['vld'] = 5

