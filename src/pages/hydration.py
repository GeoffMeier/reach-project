from datetime import datetime, time
from zoneinfo import ZoneInfo

# Variables 

def hydration_menu():
  userID = None 
  currentDate = datetime.now(ZoneInfo("America/Chicago")).date() 
  waterScore = 0 
  daily_water_target_oz = None 
  water_intake_oz = 0 
  water_entries = []
  nextReminder = None 
  reminder_trip = False # Reminder flag

  print(f"{currentDate.strftime('%B %d, %Y')}\n")

  while True:
    print("===== Hydration Menu =====\n")
    if nextReminder is not None and not reminder_trip: # Check if its time for hydrate reminder
      reminder_trip = check_reminder(nextReminder)

    if daily_water_target_oz is not None and daily_water_target_oz > 0:
      progress = (water_intake_oz / daily_water_target_oz) * 100
      waterScore = int((progress / 100) * 10000)
      if waterScore > 10000:
        waterScore = 10000
    else:
      progress = 0
      waterScore = 0
      daily_water_target_oz = daily_water_target_oz or 0

    current_time = datetime.now(ZoneInfo("America/Chicago"))
    reminder_clock = time(nextReminder[0], nextReminder[1]) if nextReminder else None

    print("1. Set Hydration Goal") # print main hydration menu
    print("2. Schedule Reminder")
    print("3. Add/Clear Water Entry")
    print("4. Show Hydration Summary")
    print("5. Return to Main Menu\n")

    choice = input("Enter selection (1-4): ") # user selection

    if choice == '1':
      daily_water_target_oz = set_goal()
      print("<<< Goal Saved >>>\n")
    elif choice == '2':
      nextReminder = schedule_reminder()
      reminder_trip = False
    elif choice == '3':
      water_intake_oz, water_entries = add_edit_water_entry(water_intake_oz, water_entries)
    elif choice == '4':
      hydration_summary(current_time, reminder_clock, daily_water_target_oz, water_intake_oz, waterScore, progress, water_entries)
    elif choice == '5':
      break
    else:
      print("[Invalid selection. Please try again.]\n")


def set_goal(): # setting hydration goal
  daily_water_target_oz = int(input("\nEnter hydration goal (in ounces): "))
  return daily_water_target_oz

def add_edit_water_entry(water_intake_oz, water_entries): # adding or clearing water entries
  while True:
    print("\n===== Add/Edit Water Entry =====\n")

    print("1. Add Water Entry")
    print("2. Clear Water Entries")
    print("3. Return to Main Menu\n")

    choice = input("Enter selection (1-3): ")

    if choice == '1': # user selection
      water_intake_oz, water_entries = add_water(water_intake_oz, water_entries)
      print(f"<<< Water Added. Your current water total is: {water_intake_oz}oz >>>")
    elif choice == '2':
      water_intake_oz, water_entries = clear_water()
      print("<<< Water Cleared >>>\n")
    elif choice == '3':
      print("\n")
      return water_intake_oz, water_entries
    else:
      print("[Invalid input. Please try again.]\n")

def add_water(water_intake_oz, water_entries): # adding water entry
  while True:
    try:
      amount = int(input("\nEnter amount of water (in ounces): "))
      water_intake_oz += amount
      timestamp = datetime.now().strftime("%H:%M:%S")
      water_entries.append((timestamp, amount))
      return water_intake_oz, water_entries
    except ValueError:
      print("[Invalid input. Please enter a valid number.]\n")

def clear_water(): # clearing water entries
  return 0, []

def schedule_reminder(): # scheduling hydration reminder
  while True:
      try:
        print("\n=== Set Reminder Time ===")
        hour = int(input("Enter the hour (1-12): "))
        minute = int(input("Enter the minute (0-59): "))
        am_pm = input("Enter AM or PM: ").strip().upper()

        if hour < 0 or hour > 12: # data validation
          print("[Hour must be between 1 and 12]")
          continue

        if minute < 0 or minute > 59: # data validation
          print("[Minutes must be between 0 and 59.]")
          continue

        if am_pm not in ["AM", "PM"]: # data validation
          print("[Invalid input. Please enter AM or PM.]")
          continue

        if am_pm == "PM" and hour != 12: # time conversion
          hour_24 = hour + 12
        if am_pm == "AM" and hour == 12: # time conversion
          hour_24 = 0

        reminder_time = time(hour_24, minute)

        print(f"\n[Reminder set for {reminder_time.strftime('%I:%M %p')}]\n")
        return hour_24, minute

      except ValueError:
        print("[Invalid input. Please enter a valid number.]\n") # data validation

def check_reminder(nextReminder):
  if not nextReminder:
    return False 

  current_time = datetime.now(ZoneInfo("America/Chicago")) # central time zone
  reminder_hour, reminder_minute = nextReminder
  reminder_clock = time(reminder_hour, reminder_minute)

  if current_time.time() >= reminder_clock: # compare time against reminder
    print(">>> Reminder: Time to hydrate! <<<\n")
    return True

  return False

def hydration_summary(current_time, reminder_clock, daily_water_target_oz, water_intake_oz, waterScore, progress, water_entries): # display hydration summary
  print("\n=== Hydration Summary ===\n")
  print("Current time:", current_time.strftime('%I:%M %p'),"\n")

  if reminder_clock:
    print("Reminder time:", reminder_clock.strftime('%I:%M %p'), "\n")
  else:
    print("Reminder time: [No Reminder Set]\n")

  print(f"Your Hydration goal for today is: {daily_water_target_oz} ounces\n")
  print(f"You current water intake: {water_intake_oz} ounces\n")
  print(f"You are at {progress:.1f}% of your goal\n")
  print(f"Your Hydration score is: {waterScore}\n")
  print("<<< Water Entries >>>")
  if not water_entries:
      print("[No Entries Submitted]")
  else:
    for timestamp, amount in water_entries:
      print(f"{timestamp}: {amount} ounces")
  print()

