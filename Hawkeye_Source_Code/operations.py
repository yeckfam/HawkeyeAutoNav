__author__ = 'tianlan'

import serial
import time

ser = serial.Serial('/dev/ttyACM0', '57600')

init_thr = 1000
hover_thr = 1500
rise_thr = hover_thr + 5
drop_thr = hover_thr - 5


#chksum calculation
def chksum(str):
    c = 0
    for a in str:
        c = ((c + ord(a)) << 1)% 256
    return c

def submit_cmd (p):
    str = "%d,%d,%d,%d" % (p['roll'], p['pitch'], p['thr'], p['yaw'])
    chk = chksum(str)
    output = "%s*%2x\r\n" % (str, chk)
    print (output)
    ser.write(output)
    ser.flush()
    time.sleep(0.1)

def operations_cleanup() :
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : 0, 'thr' : init_thr}
    submit_cmd(p)

def take_off ():
    print "take_off"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : 0, 'thr' : init_thr}
    while (p['thr'] < hover_thr):
        p['thr'] += 10
        submit_cmd(p)
    hover()

def landing ():
    print "landing"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : 0, 'thr' : drop_thr}
    while (p['thr'] > init_thr):
        p['thr'] -= 10
        submit_cmd(p)

def hover ():
    print "hover"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)

def rise ():
    print "rise"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : 0, 'thr' : rise_thr}
    submit_cmd(p)

def drop ():
    print "drop"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : 0, 'thr' : drop_thr}
    submit_cmd(p)

def turn_left ():
    print "turn_left"
    p = {'roll' : -5, 'pitch' : 0, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)

def turn_right ():
    print "turn_right"
    p = {'roll' : 5, 'pitch' : 0, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)

def spin_left ():
    print "spin_left"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : -10, 'thr' : hover_thr}
    submit_cmd(p)

def spin_right ():
    print "spin_right"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : 10, 'thr' : hover_thr}
    submit_cmd(p)

def move_forward ():
    print "move_forward"
    p = {'roll' : 0, 'pitch' : -1, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)

def move_backward ():
    print "move_backward"
    p = {'roll' : 0, 'pitch' : 1, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)

