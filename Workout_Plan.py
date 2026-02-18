import random
import time


#This section is the workout level "Easy, Medium, and Hard", also contains the workout routine at each level
workout_level = {
    "Easy": [
        ["treadmill walk", "hits workout", "15 squats"],
        ["hit workout", "15 squats", "10 push-ups"],
        ["treadmill walk", "hits workout", "20 sit-ups"]
    ],

    "Medium": [
        ["weights", "hits", "15 squats", "10 push-ups", "20 sit-ups"],
        ["treadmill jog", "10 lunges", "15 jumping jacks", "10 mountain climbers"],
        ["cycling", "50 flutter kicks", "10 push-ups", "wall sit"]
    ],

    "Hard": [
        ["stairmaster", "weights", "15 squats", "wall sit", "20 push-ups"],
        ["treadmill run", "50 crunches", "50 squats", "cycling", "30 sit-ups"],
        ["stairmaster", "60 second plank", "30 squats", "20 push-ups", "yoga"]
    ]

    }
#This is a timer that starts at the beginning of the workout and goes for however long the user inputted 
def countdown(minutes):
    t = minutes * 60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Workout complete!")

#This is section is for the user to see on the screen their outputted level that they have selected, and also for them to see their workout out routine
#User will also have a customized score based on their difficulty level they chose to go with
def start_workout(user, difficulty_level):
    selected_excersise = random.choice(workout_level[difficulty_level])
    total_time = 0
    
    print(f"Your customized {difficulty_level} workout will begin now!")

    for exercise in selected_excersise:
        print(f"Current Activity: {exercise}")

        minutes = int(input(f"How many minutes for {exercise}? "))

        countdown(minutes)

        total_time += minutes


    if difficulty_level == "Easy":
        exercise_score = 20
    elif difficulty_level == "Medium":
        exercise_score = 40
    elif difficulty_level == "Hard":
        exercise_score = 70
    else:
        exercise_score = 0

    user.set_exercise_score(exercise_score)

    print(f"You have completed your workout! {exercise_score} will be added to you exercise points.")

    return total_time, exercise_score

    
#This is where the user will be able to pick which level they prefer to workout at, and also for them to actually see their workout routine.
while True:
    print("-" * 25)
    print("1. Start Easy Workout")
    print("2. Start Medium Workout")
    print("3. Start Hard Workout")
    print("4. Exit")

    user_choice = input("Choose level you would like to workout at (1. Easy, 2.Medium, 3. Hard, 4. Exit):")

    if user_choice == "1":
        start_workout("Easy")

    elif user_choice == "2":
        start_workout("Medium")


    elif user_choice == "3":
        start_workout("Hard")


    elif user_choice == "4":
        print("Goodbye!")
        break




