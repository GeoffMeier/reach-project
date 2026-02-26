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
        ["weights", "hit workout", "15 squats", "10 push-ups", "20 sit-ups"],
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
def start_workout(difficulty_level, total_min, daily_targ_min):
    selected_excersise = random.choice(workout_level[difficulty_level])
    session_min = 0
    
    print(f"Your customized {difficulty_level} workout will begin now!")

    for exercise in selected_excersise:
        print(f"Current Activity: {exercise}")

        minutes = int(input(f"How many minutes for {exercise}? "))

        countdown(minutes)

        session_min += minutes

    new_total_min = total_min + session_min


    if daily_targ_min > 0:
        
        exercise_score = int((session_min / daily_targ_min) * 10000)

        if exercise_score > 10000:
            exercise_score = 10000
    else:
        exercise_score = 0

    
    print(f"You've completed {session_min} minutes for this session!")
    print(f"You have completed your workout! {exercise_score} will be added to you exercise points.")
    print(f"You have workouted out for a total of: {new_total_min} minutes")

    return new_total_min, exercise_score

total_min = 0
daily_targ_min = 30
total_score = 0
    
#This is where the user will be able to pick which level they prefer to workout at, and also for them to actually see their workout routine.
def workoutmenu(username):
    global total_min, total_score
    while True:
        print("-" * 25)
        print("1. Start Easy Workout")
        print("2. Start Medium Workout")
        print("3. Start Hard Workout")
        print("4. Exit")

        user_choice = input("Choose level you would like to workout at (1. Easy, 2. Medium, 3. Hard, 4. Exit):")

        if user_choice == "1":
            total_min, earned_score = start_workout("Easy", total_min, daily_targ_min)
            total_score += earned_score

        elif user_choice == "2":
            total_min, earned_score =start_workout("Medium", total_min, daily_targ_min)
            total_score += earned_score


        elif user_choice == "3":
            total_min, earned_score =start_workout("Hard", total_min, daily_targ_min)
            total_score += earned_score


        elif user_choice == "4":
            print(f"Goodbye! Final Score: {total_score}")

            from pages.auth import update_user_field
            update_user_field(username, "exercise_score", total_score)

            break
        else:
            print("Invalid selection. please choose between 1, 2, 3, 4.")



