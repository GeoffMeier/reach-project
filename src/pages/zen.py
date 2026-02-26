import time
import math
from datetime import date

# Initialize variables

scheduled_date = 0

time_remaining = 0
time_elapsed = 0
daily_target = 600


zen_score = 0
mode_select = 0

def clamp_0_10000(x):
    return max(0, min(10000, x))

def current_date():
    print(date.today())

def set_time():
    global time_remaining
    print("set time (seconds):")
    time_remaining = int(input())
    
def set_target():
    global daily_target
    print("set daily target (seconds)")
    daily_target = int(input())

def start():
    global time_remaining, time_elapsed, zen_score, daily_target

    time_elapsed = 0  # reset each session

    while time_remaining > 0:
        time_elapsed += 1

        if daily_target <= 0:
            zen_score = 0
        else:
            zen_score = (10000 * math.sqrt(time_elapsed / daily_target))

        zen_score = clamp_0_10000(zen_score)

        print(f"Time left: {time_remaining} seconds, score {zen_score:.0f}", end="\r")

        time.sleep(1)
        time_remaining -= 1

    print(" " * 50, end="\r")  # clear line
    print(f"Timer finished. Score: {zen_score:.0f}")
    return int(zen_score)
    


        
def menu(username):
    while True:
        print("1. display date\n2. set time\n3. start\n4. set daily target\n5. quit")
        mode_select = int(input())
        if mode_select == 1:
            current_date()
        elif mode_select == 2:
            set_time()
        elif mode_select == 3:
            score = start()

            if score is not None:
                from pages.auth import update_user_field
                update_user_field(username, "zen_score", score)
        elif mode_select == 4:
            set_target()
        elif mode_select == 5:
            break