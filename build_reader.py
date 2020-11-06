import datetime
import sc_bo_utils
import time as os_time
from threading import Timer
from subprocess import call
import sys

def perform_action(printed_statement, spoken_text):
    print(printed_statement)
    call(["python3", "tts.py", spoken_text])

def read(build_file, shorthand, supply, delay, scaling):
    print("Press enter to begin: ", end = '')
    input()

    with open('builds/' + build_file, 'r') as build_order:
        print("Build start.")
        call(["python3", "tts.py", "Build start."])

        for row in build_order.readlines():
            # Formatting
            row = sc_bo_utils.cleanup_row(row)
            row = row.split(",")

            # Timers for speech
            timer_length = sc_bo_utils.generate_timer_duration(row[1], delay, scaling)

            # Read action
            actions = ','.join(row[2:])
            printed_text = sc_bo_utils.generate_reminder_line(row[1], scaling, row[0], actions)

            if shorthand:
                actions = sc_bo_utils.to_shorthand(actions)
            if supply:
                actions = row[0] + " " + actions
            Timer(timer_length, perform_action, args=[printed_text, actions]).start()
