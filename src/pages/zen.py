import time
import math
from datetime import date
import winsound

# Initialize variables

scheduled_date = 0

time_remaining = 0
time_elapsed = 0
daily_target = 600


zen_score = 0
mode_select = 0

beeps = 3

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

        print(f"Time left: {time_remaining} seconds ", end="\r")

        time.sleep(1)
        time_remaining -= 1
        
    winsound.Beep(300, 1000)
    print(" " * 100, end="\r")  # clear line
    print(f"\nTimer finished. Score: {zen_score:.0f}")
    time.sleep(2)
    return int(zen_score)
    
def set_reminder():
    reminder_time = 0

    print("\nSet a duration for the reminder (minutes): ")
    reminder_time = float(input()) * 60
    print(f"Reminder set for {reminder_time / 60} minutes.\n")
    
    while reminder_time > 0:
        time.sleep(1)
        reminder_time -= 1
    
    if reminder_time == 0:
        while beeps > 0:
            winsound.Beep(500, 400)
            time.sleep(0.4)
            beeps -= 1

        print("\nReminder time finished.")
        beeps = 3
    

        
def menu(username):
    while True:
        print("\n1. Display date\n2. Set time\n3. Start\n4. Set daily target\n5. Set reminder\n6. Exit")
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
            set_reminder()
        elif mode_select == 6:
            break