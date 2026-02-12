from pages.Hydration import hydration_menu
from pages.workout import start_exercise_menu
from pages.zen import zen_menu


def home_menu():

    while True:

        print("Welcome to Reach!\n")
        print("===== Home Page =====\n")
        print("1. Meal Plan")
        print("2. Hydration")
        print("3. Workouts")
        print("4. Zen")
        print("5. REACH Score")
        print("0. Logout")
        
        choice = input("Select option: ")

        if choice == "1":
            
            print("Access granted.")
            break

        elif choice == "2":
            hydration_menu()
            break

        elif choice == "3":
            start_exercise_menu()   

        elif choice == "4":
            zen_menu()
            break
        elif choice == "5":
            #Need to implement REACH score calculation and display
            print("REACH SCORE")
            break
        elif choice == "0":
            print("Logging out...")
            break


        else:
            print("Invalid selection.")
