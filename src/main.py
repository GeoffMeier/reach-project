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
        print(self.reach_score)




#NOTE: User login page should declare this object with these variables
user = User("one", "two", "three", "four", "five", "a", 42, 1.5, 99.9)

#Test
print(user.__dict__)
print(user.reach_score)
user.set_food_score(1.2)
user.get_food_score()
user.get_water_score()


# main.py
import sys
from pages.auth import start_auth_page

if __name__ == "__main__":
    start_auth_page()  # Start the program
 
def main():
    modesel = 0
    print("Select a mode:\n1. Hydration mode\n2. Meal Plan\n3. Workout plan\n4. Zen mode\n5. Authentication\n6. Reach score\n7. Exit\n")
    modesel = int(input())
    
    if modesel == 1:
        #CALL HYDRATION HERE
        pass
    elif modesel == 2:
        #CALL MEALPLAN HERE
        pass
    elif modesel == 3:
        #CALL WORKOUT PLAN HERE
        pass
    elif modesel == 4:
        #CALL ZEN MODE HERE
        pass
    elif modesel == 5:
        #CALL AUTH HERE
        pass
    elif modesel == 6:
        user.print_reach_score()
    elif modesel == 7:
        sys.exit()

main()