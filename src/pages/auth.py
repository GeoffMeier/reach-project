import json
import os
from pages.home import home_menu
USERS_FILE = "users.txt"
users = {}

def load_users():
    global users
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}
    else:
        users = {}
    for user in users.values():
        user.setdefault("food_score", 0.0)
        user.setdefault("exercise_score", 0.0)
        user.setdefault("water_score", 0.0)
        user.setdefault("zen_score", 0.0)
        user.setdefault("reach_score", 0.0)

def save_users():
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def update_user_field(username, field_name, new_value):
    load_users()

    if username not in users:
        print("User not found.")
        return

    if field_name not in users[username]:
        print("Invalid field.")
        return

    users[username][field_name] = new_value
    save_users()        


def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid input. Please enter text.")

def get_char(prompt):
    while True:
        value = input(prompt).strip().lower()
        if len(value) == 1 and value in ["m", "f", "o"]:
            return value
        print('Invalid input. Enter "m" (male), "f" (female), or "o" (other).')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number. Please enter an integer.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a decimal value.")

def get_date(prompt):
    while True:
        value = input(prompt)
        parts = value.split("-")
        if len(parts) == 3 and all(p.isdigit() for p in parts):
            return value
        print("Invalid date. Use format YYYY-MM-DD.")


def create_account():
    load_users()
    user_id = len(users) + 1

    print("\n--- Create Account ---")
    username = get_string("Username: ")

    if username in users:
        print("Username already exists.")
        return

    password = get_string("Password: ")
    birth_date = get_date("Birth Date (YYYY-MM-DD): ")
    sex = get_char("Sex (M/F/O): ")
    first_name = get_string("First Name: ")
    last_name = get_string("Last Name: ")
    height_inches = get_int("Height (inches): ")
    weight_lbs = get_float("Weight (lbs): ")
    target_weight_lbs = get_float("Target Weight (lbs): ")

    
    users[username] = {
        "userID": user_id,
        "username": username,
        "password": password,
        "birth_date": birth_date,
        "sex": sex,
        "first_name": first_name,
        "last_name": last_name,
        "height_inches": height_inches,
        "weight_lbs": weight_lbs,
        "target_weight_lbs": target_weight_lbs,
        "food_score": 0.0,
        "exercise_score": 0.0,
        "water_score": 0.0,
        "zen_score": 0.0,
        "reach_score": 0.0
    }

    save_users()
    print("Account created successfully!")


def login():
    load_users()
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"\nWelcome {users[username]['first_name']}!")
        print(f"User ID: {users[username]['userID']}")
        return username   # ✅ return username instead of True
    else:
        print("Invalid username or password.")
        return None


def start_auth_page():
    load_users()
    print(users)
    while True:
        print("\n=== REACH ===")
        print("1. Login")
        print("2. Create Account")
        print("0. Exit")

        choice = input("Select option: ")
        if choice == "1":
            username = login()
            if username:
                print("Access granted.")
                home_menu(username)   # ✅ pass username
                
        elif choice == "2":
            create_account()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid selection.")
