import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

class User:
    def __init__(
        self,
        username: str,
        password: str,
        birth_date: str,
        sex: str,
        first_name: str,
        last_name: str,
        height_inches: int,
        weight_lbs: float,
        target_weight_lbs: float,
        food_score: float = 0,
        exercise_score: float = 0,
        water_score: float = 0,
        zen_score: float = 0,
        reach_score: float = 0
    ):
        
        self.username = username
        self.password = password
        self.birth_date = birth_date
        self.sex = sex
        self.first_name = first_name
        self.last_name = last_name
        self.height_inches = height_inches
        self.weight_lbs = weight_lbs
        self.target_weight_lbs = target_weight_lbs
        self.food_score = food_score
        self.exercise_score = exercise_score
        self.water_score = water_score
        self.zen_score = zen_score
        self.reach_score = reach_score
    
    #TODO: PLUG ME IN!
    def set_food_score(self, a):
        self.food_score = a
        
    def set_exercise_score(self, a):
        self.exercise_score = a
        
    def set_water_score(self, a):
        self.water_score = a
        
    def set_zen_score(self, a):
        self.zen_score = a    


    
    def get_food_score(self):
        print(self.food_score)
        
    def get_exercise_score(self):
        print(self.exercise_score)
        
    def get_water_score(self):
        print(self.water_score)
        
    def get_zen_score(self):
        print(self.zen_score)  
        
    def calc_reach_score(self):
        self.reach_score = (self.food_score * 3) + (self.water_score * 3.5) + (self.exercise_score * 2.5) + self.zen_score
    
    def print_reach_score(self):
        print("Reach score: {self.reach_score}")




#NOTE: User login page should declare this object with these variables
user = User("one", "two", "three", "four", "five", "a", 42, 1.5, 99.9)





from pages.auth import start_auth_page
import hydration
import Meal_Plan
import Workout_Plan
import zen
 
def main():
    modesel = 0
    while True:
        print("Select a mode:\n1. Hydration mode\n2. Meal Plan\n3. Workout plan\n4. Zen mode\n5. Reach score\n6. Exit\n")
        modesel = int(input())
        
        if modesel == 1:
            hydration.hydration_menu()
            
        elif modesel == 2:
            Meal_Plan.mealmenu()

        elif modesel == 3:
            Workout_Plan.workoutmenu()
            
        elif modesel == 4:
            zen.menu()
            
        elif modesel == 5:
            User.print_reach_score()
            
        elif modesel == 6:
            sys.exit()

if __name__ == "__main__":
    start_auth_page()  # Start the program
    main()