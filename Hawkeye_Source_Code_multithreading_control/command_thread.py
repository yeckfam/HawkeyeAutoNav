__author__ = 'tianlan'

import operations
import time
import configuration

def command_thread_wrapper_function (distance, keyboard_cmd, db, goback_cmd):
    prevCmdName = ''
    db_entry = {'cmd': '', 'start_loc': [0, 0, 0, 0, 0, 0]}
    while True:
        if (goback_cmd['vld'] == 0):
            # Step 1: Get range
            # for i in range (0, configuration.config['num_directions']):
            #     print "Command_Thread::::Tian:: i = ", i, "distance[i] = ", distance[i]
            # Step 2: Come up with commands
            # Step 3: Issue commands
            if (keyboard_cmd['vld'] == 0):
                cmdToIssue = getattr(operations, 'hover')
            elif ((keyboard_cmd['vld'] > 0) & (keyboard_cmd['cmd'] == 'w')):
                cmdToIssue = getattr(operations, 'move_forward')
                keyboard_cmd['vld'] = keyboard_cmd['vld'] - 1
            elif ((keyboard_cmd['vld'] > 0) & (keyboard_cmd['cmd'] == 's')):
                cmdToIssue = getattr(operations, 'move_backward')
                keyboard_cmd['vld'] = keyboard_cmd['vld'] - 1
            elif ((keyboard_cmd['vld'] > 0) & (keyboard_cmd['cmd'] == 'a')):
                cmdToIssue = getattr(operations, 'turn_left')
                keyboard_cmd['vld'] = keyboard_cmd['vld'] - 1
            elif ((keyboard_cmd['vld'] > 0) & (keyboard_cmd['cmd'] == 'd')):
                cmdToIssue = getattr(operations, 'turn_right')
                keyboard_cmd['vld'] = keyboard_cmd['vld'] - 1
            elif ((keyboard_cmd['vld'] > 0) & (keyboard_cmd['cmd'] == 'q')):
                cmdToIssue = getattr(operations, 'spin_left')
                keyboard_cmd['vld'] = keyboard_cmd['vld'] - 1
            elif ((keyboard_cmd['vld'] > 0) & (keyboard_cmd['cmd'] == 'e')):
                cmdToIssue = getattr(operations, 'spin_right')
                keyboard_cmd['vld'] = keyboard_cmd['vld'] - 1
            elif ((keyboard_cmd['vld'] > 0) & (keyboard_cmd['cmd'] == 'z')):
                cmdToIssue = getattr(operations, 'rise')
                keyboard_cmd['vld'] = keyboard_cmd['vld'] - 1
            elif ((keyboard_cmd['vld'] > 0) & (keyboard_cmd['cmd'] == 'c')):
                cmdToIssue = getattr(operations, 'drop')
                keyboard_cmd['vld'] = keyboard_cmd['vld'] - 1
            else:
                cmdToIssue = getattr(operations, 'hover')
                keyboard_cmd['vld'] = 0
            cmdToIssue()
            # Step 4: If command changed, store to db
            if (cmdToIssue.__name__ != prevCmdName):
                db_entry['cmd'] = cmdToIssue.__name__
                db_entry['start_loc'] = distance
                db.append(db_entry)
                prevCmdName = cmdToIssue.__name__
                print prevCmdName, 'is added into db'
        else:
            if (len(db) == 0):
                cmdToIssue = getattr(operations, 'hover')
            else:
                db_entry = db.pop()
                print db_entry['cmd']
                cmdToIssue = getattr(operations, db_entry['cmd'])
            cmdToIssue()
