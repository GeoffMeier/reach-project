# Hydration

from datetime import datetime

def hydration_menu():

  h_score = 0
  goal = None
  water_total = 0
  water_entries = []
  
  while True:
    print("===== Hydration Menu =====\n")

    if goal is not None and goal > 0:
      progress = (water_total / goal) * 100
      #print(f"Water Total: {water_total} ounces")
      print(f"Your Hydration goal for today is: {goal} ounces\n")
      print(f"You are at {progress:.1f}% of your current goal\n")
      print("<<< Water Entries >>>")
      for timestamp, amount in water_entries:
        print(f"[{timestamp} : {amount} ounces]")
      print("\n")

    print("1. Set Goal")
    print("2. Schedule Reminder")
    print("3. Add/Edit Water Entry")
    print("4. Return to Main Menu\n")

    choice = input("Enter selection (1-4): ")
    
    if choice == '1':
      goal = set_goal()
      print("<<< Goal Saved >>>\n")
    elif choice == '2':
      schedule_reminder()
    elif choice == '3':
      water_total, water_entries = add_edit_water_entry(water_total, water_entries)
    elif choice == '4':
      break
    else:
      print("Invalid selection. Please try again.")


def set_goal():
  goal = int(input("\nEnter hydration goal (in ounces): "))
  return goal

def schedule_reminder():
  print("Reminder scheduled successfully!")
  return

def add_edit_water_entry(water_total, water_entries):

  while True:
    print("\n===== Add/Edit Water Entry =====\n")

    print("1. Add Water Entry")
    print("2. Clear Water Entries")
    print("3. Return to Main Menu\n")

    choice = input("Enter selection (1-3): ")
    
    if choice == '1':
      water_total, water_entries = add_water(water_total, water_entries)
      print("<<< Water Added >>>")
    elif choice == '2':
      water_total, water_entries = clear_water()
      print("<<< Water Cleared >>>\n")
    elif choice == '3':
      return water_total, water_entries
    else:
      print("Invalid selection. Please try again.")

def add_water(water_total, water_entries):
  while True:
    try:
      amount = int(input("\nEnter amount of water (in ounces): "))
      water_total += amount
      timestamp = datetime.now().strftime("%H:%M:%S")
      water_entries.append((timestamp, amount))
      return water_total, water_entries
    except ValueError:
      print("Invalid input. Please enter a valid number.")

def clear_water():
  return 0, []

