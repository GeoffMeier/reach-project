from pages.hydration import hydration_menu
from pages.zen import menu
from pages.meal_plan import mealmenu
from pages.workout_plan import workoutmenu


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
            print(f"Your REACH Score: {users[username]['reach_score']}")
        elif choice == "0":
            print("Logging out...")
            break

        else:
            print("Invalid selection.")