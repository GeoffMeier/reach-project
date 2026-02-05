users = {}
# Helper functions for input validation
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

        if len(parts) == 3:
            year, month, day = parts
            if year.isdigit() and month.isdigit() and day.isdigit():
                return value

        print("Invalid date. Use format YYYY-MM-DD.")


#Create account function for auth page
def create_account():
    user_id = 1

    print("\n--- Create Account ---")

    username = get_string("Username: ")

    if username in users:
        print("Username already exists.")
        return

    password = get_string("Password: ")
    birth_date = get_date("Birth Date (YYYY-MM-DD): ")
    sex = get_char("Sex (M/F): ")
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
        "target_weight_lbs": target_weight_lbs
    }

    user_id += 1

    print("Account created successfully!")

#Login function for auth page
def login():
    print("\n--- Login ---")

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"\nWelcome {users[username]['first_name']}!")
        print(f"User ID: {users[username]['userID']}")
        return True
    else:
        print("Invalid username or password.")
        return False

#Authentication page
def start_auth_page():
    print(users)
    while True:
        print("\n=== REACH Wellness Platform ===")
        print("1. Login")
        print("2. Create Account")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            if login():
                print("Access granted.  ")
                break

        elif choice == "2":
            create_account()

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid selection.")



    
    