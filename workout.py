import random
import time


class Workout:  


    workout_level = {
        
        "Easy": [
            ["10 min treadmill walk", "5 min hits", "15 squats"],
            ["15 min hits", "15 squats", "10 push-ups"],
            ["10 min treadmill walk", "5 min hits", "20 sit-ups"]
        ],

        "Medium": [
            ["10 min weights", "10 min hits", "15 squats", "10 push-ups", "20 sit-ups"],
            ["10 min treadmill jog", "10 lunges", "15 jumping jacks", "10 mountain climbers"],
            ["25 min cycling", "50 flutter kicks", "10 push-ups", "3 min wall sit"]
        ],

        "Hard": [
            ["15 min stairmaster", "15 min weights", "15 squats", "5 min wall sit", "20 push-ups"],
            ["15 min treadmill run", "50 crunches", "50 squats", "10 min cycling", "30 sit-ups"],
            ["10 min stairmaster", "60 second plank", "30 squats", "20 push-ups", "10 min yoga"]
        ]

    }
    def __init__(self, level):
        self.level = level
        self.workouts = random.choice(Workout.workout_level[level])

    def countdown(self, minutes):
        t = minutes * 60

        while t:
           mins, secs = divmod(t, 60)
           timer = '{:02d}:{:02d}'.format(mins, secs)
           print(timer, end="\r")
           time.sleep(1)
           t -= 1
        print("Workout complete!")

    def start_excersise(self):

        print(f"starting workout")
        for exercise in self.workouts:
            print(f"Exercise: {exercise}:")  
            duration = input(f"Enter time for workout {exercise}:")
            self.countdown(int(duration))
        print("\n You have completed the workout! Good work!")

    
    def main():

        while True:
            print("-" * 25)
            print("1. Start Easy Workout")
            print("2. Start Medium Workout")
            print("3. Start Hard Workout")
            print("4. Exit")

            user_choice = input("Choose level you would like to workout at (1. Easy, 2.Medium, 3. Hard, 4. Exit):")

            if user_choice == "1":
                Workout("Easy").start_exercise()

            elif user_choice == "2":
                Workout("Medium").start_exercise()

            elif user_choice == "3":
                Workout("Hard").start_exercise()

            elif user_choice == "4":
                print("Exiting workout, Goodbye!")
                break




   



