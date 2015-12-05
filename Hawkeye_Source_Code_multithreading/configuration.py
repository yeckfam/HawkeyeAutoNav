__author__ = 'tianlan'

config = {}

#========================================================
# Initialization
#========================================================
# initialization setup time before taking off in seconds
config['setup_time'] = 5

#========================================================
# Main
#========================================================
# overall timeout value after taking off in seconds
config['runtime'] = 10

#========================================================
# Operations
#========================================================
# initial throttle
config['init_thr'] = 1000

# hover throttle
config['hover_thr'] = 1600

# take off throttle increment step
config['take_off_thr_step'] = 10

# landing throttle decrement step
config['landing_thr_step'] = -10

# rise throttle increment step
config['rise_thr_step'] = 5

# drop throttle decrement step
config['drop_thr'] = -5

# turn left roll decrement step
config['turn_left_roll_step'] = -5

# turn right roll increment step
config['turn_right_roll_step'] = 5

# spin left yaw decrement step
config['spin_left_yaw_step'] = -10

# spin right yaw increment step
config['spin_right_yaw_step'] = 10

# move forward pitch decrement step
config['move_forward_pitch_step'] = -1

# move backward pitch increment step
config['move_backward_pitch_step'] = 1

#========================================================
# Range Sensor
#========================================================
# directions
config['directions'] = ['front', 'back', 'right', 'left', 'top', 'bottom']
config['num_directions'] = 6

# range sensor GPIO pin assignment
config['TRIG'] = (23, 25, 16, 21, 17, 13)
config['ECHO'] = (24, 12, 20, 26, 27, 19)

# range sensor detect time gap in seconds
config['range_sensor_detect_gap'] = 0.05
