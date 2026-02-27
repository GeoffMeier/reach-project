from pages.hydration import hydration_menu
from pages.zen import menu
from pages.meal_plan import mealmenu
from pages.workout_plan import workoutmenu
import random
import time

def quotes(score):
    quotes_by_score = {
    1: [
        "The journey is long, but every path begins with a single step.",
        "Your goals may feel distant, but direction matters more than speed.",
        "Focus on learning — results will come in time.",
        "Today is about planting seeds, not harvesting.",
        "Progress may be invisible now, but it's still happening."
    ],
    2: [
        "You're moving forward, even if the finish line is far away.",
        "The gap is shrinking — keep building.",
        "Momentum is forming beneath the surface.",
        "Each effort makes the mountain a little smaller.",
        "You're no longer at the starting line."
    ],
    3: [
        "You're halfway closer than you think.",
        "The goal is no longer abstract — it's taking shape.",
        "Your consistency is turning possibility into probability.",
        "You can almost see the results forming.",
        "What once felt impossible now feels achievable."
    ],
    4: [
        "The finish line is in sight.",
        "You're operating at the level you once admired.",
        "Your goal is within reach — stay steady.",
        "The breakthrough is closer than your doubts suggest.",
        "You are stepping into the version of yourself you aimed for."
    ],
    5: [
        "You're on the edge of success — one more push.",
        "The goal is right in front of you.",
        "You've built the momentum — now claim the result.",
        "This is the moment your past effort prepared you for.",
        "You are arriving — don't slow down now."
    ]
    }
    
    if score < 20000:
        print(quotes_by_score[1][random.randrange(0, 5)])
    elif score < 40000:
        print(quotes_by_score[2][random.randrange(0, 5)])
    elif score < 60000:
        print(quotes_by_score[3][random.randrange(0, 5)])
    elif score < 80000:
        print(quotes_by_score[4][random.randrange(0, 5)])
    elif score <= 100000:
        print(quotes_by_score[5][random.randrange(0, 5)])
    time.sleep(3)
        
def home_menu(username):
    while True:
        print("\n===== HOME PAGE =====")
        print("1. Meal Plan")
        print("2. Hydration")
        print("3. Workouts")
        print("4. Zen")
        print("5. REACH Score")
        print("0. Logout")

        choice = input("Select option: ")

        if choice == "1":
            mealmenu(username)

        elif choice == "2":
            hydration_menu(username)

        elif choice == "3":
            workoutmenu(username)

        elif choice == "4":
            menu(username)

        elif choice == "5":
            from pages.auth import load_users, users
            load_users()
            users[username]['reach_score'] = ((3 * (users[username]['food_score'] + 1) - 3)+ (2.5 * (users[username]['water_score'] + 1) - 2.5)+ (2.5 * (users[username]['exercise_score'] + 1) - 2.5)+ (2 * (users[username]['zen_score'] + 1) - 2))
            print(f"\nYour REACH Score: {users[username]['reach_score']:.0f}")
            quotes(users[username]['reach_score'])
        elif choice == "0":
            print("Logging out...")
            break

        else:
            print("Invalid selection.")