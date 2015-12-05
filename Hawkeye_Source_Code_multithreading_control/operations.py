__author__ = 'tianlan'

import serial
import time
import configuration

ser = serial.Serial('/dev/ttyACM0', '57600')

init_thr = configuration.config['init_thr']
hover_thr = configuration.config['hover_thr']

take_off_thr_step = configuration.config['take_off_thr_step']
landing_thr_step = configuration.config['landing_thr_step']

rise_thr = hover_thr + configuration.config['rise_thr_step']
drop_thr = hover_thr + configuration.config['drop_thr_step']

turn_left_roll_step = configuration.config['turn_left_roll_step']
turn_right_roll_step = configuration.config['turn_right_roll_step']
spin_left_yaw_step = configuration.config['spin_left_yaw_step']
spin_right_yaw_step = configuration.config['spin_right_yaw_step']
move_forward_pitch_step = configuration.config['move_forward_pitch_step']
move_backward_pitch_step = configuration.config['move_backward_pitch_step']

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
        p['thr'] += take_off_thr_step
        submit_cmd(p)
    hover()

def landing ():
    print "landing"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : 0, 'thr' : drop_thr}
    while (p['thr'] > init_thr):
        p['thr'] += landing_thr_step
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
    p = {'roll' : turn_left_roll_step, 'pitch' : 0, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)

def turn_right ():
    print "turn_right"
    p = {'roll' : turn_right_roll_step, 'pitch' : 0, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)

def spin_left ():
    print "spin_left"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : spin_left_yaw_step, 'thr' : hover_thr}
    submit_cmd(p)

def spin_right ():
    print "spin_right"
    p = {'roll' : 0, 'pitch' : 0, 'yaw' : spin_right_yaw_step, 'thr' : hover_thr}
    submit_cmd(p)

def move_forward ():
    print "move_forward"
    p = {'roll' : 0, 'pitch' : move_forward_pitch_step, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)

def move_backward ():
    print "move_backward"
    p = {'roll' : 0, 'pitch' : move_backward_pitch_step, 'yaw' : 0, 'thr' : hover_thr}
    submit_cmd(p)
