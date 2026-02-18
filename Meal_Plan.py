import random

Meal_Plan = {
        
        "Protein": {
            "Breakfast":[
                {"name": "Oatmeal with Banana", "calories": 315, "protein": 11, "fiber": 7, "carbs": 35 },
                {"name": "Greek Yougurt Parfait", "calories": 250, "protein": 15, "fiber": 25, "carbs": 22}
            ],

            "Lunch":[
                {"name": "Tuna Advocado Wrap", "calories": 435, "protein": 35, "fiber": 10, "carbs": 40 },
                {"name": "Grilled Chicken Salad", "calories": 397, "protein": 42, "fiber": 3, "carbs": 15}

           ],

           "Dinner":[
                {"name": "Skillet Salmon With Pesto Sauce", "calories": 540, "protein": 37, "fiber": 4, "carbs": 15 },
                {"name": "Chicken and Chickpea Curry", "calories": 510, "protein": 26, "fiber": 6, "carbs": 32}

           ]

        },


        "Vegan": {
            "Breakfast":[
                {"name": "Cinnamon Sugar French Toast Sticks", "calories": 330, "protein": 2, "fiber": 3, "carbs": 38 },
                {"name": "Vegan Sausage and Hash Brown Kebabs", "calories": 223, "protein": 12, "fiber": 5, "carbs": 17}
            ],

            "Lunch":[
                {"name": "Vegan Sushi Bowl", "calories": 500, "protein": 11, "fiber": 14, "carbs": 53 },
                {"name": "Vegan Burrito Bowl", "calories": 565, "protein": 16, "fiber": 24, "carbs": 70}

           ],

           "Dinner":[
                {"name": "Jackfruit Tacos", "calories": 225, "protein": 4, "fiber": 7, "carbs": 25 },
                {"name": "Tofu Fried Rice", "calories": 450, "protein": 15, "fiber": 4, "carbs": 41}

           ]

        },




        "Asian": {
            "Breakfast":[
                {"name": "Chinese Congee", "calories": 160, "protein": 2, "fiber": 1, "carbs": 35 },
                {"name": "Malaysian Kaya Toast and Eggs", "calories": 441, "protein": 15, "fiber": 2, "carbs": 40}
            ],

            "Lunch":[
                {"name": "Fresh Spring Rolls", "calories": 115, "protein": 3, "fiber": 2, "carbs": 11 },
                {"name": "Spicy Ramen", "calories": 510, "protein": 6, "fiber": 2, "carbs": 59}

           ],

           "Dinner":[
                {"name": "Thai Stir Fried Noodles", "calories": 422, "protein": 7, "fiber": 2, "carbs": 40 },
                {"name": "Korean Beef Bulgogi Rice Bowl", "calories": 570, "protein": 19, "fiber": 7, "carbs": 55}

           ]

        },



        "Italian": {
            "Breakfast":[
                {"name": "Cornetto", "calories": 280, "protein": 3, "fiber": 2, "carbs": 41 },
                {"name": "Tiroler Grostl", "calories": 630, "protein": 32, "fiber": 11, "carbs": 55}
            ],

            "Lunch":[
                {"name": "Italian Brunch Torte", "calories": 710, "protein": 33, "fiber": 6, "carbs": 55 },
                {"name": "Thyme Lemon and Scampi Bruschetta", "calories": 100, "protein": 5, "fiber": 2, "carbs": 10}

           ],

           "Dinner":[
                {"name": "Scarpariello Pasta", "calories": 435, "protein": 14, "fiber": 3, "carbs": 72 },
                {"name": "Beef Stew with Polenta", "calories": 750, "protein": 40, "fiber": 3, "carbs": 40}

           ]

        },



        "American": {
            "Breakfast":[
                {"name": "Buttermilk Pancakes with Bacon and Eggs", "calories": 925, "protein": 25, "fiber": 2, "carbs": 43 },
                {"name": "Bagel with Cream Cheese", "calories": 490, "protein": 8, "fiber": 4, "carbs": 62}
            ],

            "Lunch":[
                {"name": "Club Sandwich", "calories": 630, "protein": 33, "fiber": 4, "carbs": 45 },
                {"name": "Buffalo Wings", "calories": 452, "protein": 42, "fiber": 1, "carbs": 12}

           ],

           "Dinner":[
                {"name": "Classic Cheesburger with Fries", "calories": 1100, "protein": 44, "fiber": 10, "carbs": 110 },
                {"name": "Philly Cheesesteak", "calories": 963, "protein": 60, "fiber": 3, "carbs": 66}

           ]

        },


        "Mexican": {
            "Breakfast":[
                {"name": "Huevos Rancheros", "calories": 330, "protein": 14, "fiber": 7, "carbs": 22 },
                {"name": "Chilaquiles", "calories": 735, "protein": 31, "fiber": 9, "carbs": 59}
            ],

            "Lunch":[
                {"name": "Enchiladas Verdes", "calories": 522, "protein": 17, "fiber": 4, "carbs": 42 },
                {"name": "Tortas", "calories": 630, "protein": 44, "fiber": 6, "carbs": 61}

           ],

           "Dinner":[
                {"name": "Tacos de Suadero", "calories": 300, "protein": 22, "fiber": 11, "carbs": 15 },
                {"name": "Gringas", "calories": 280, "protein": 21, "fiber":2, "carbs": 23}

           ]

        },

 }


calorie_target = 1700
calories_consumed = 0
p_tot = 0
f_tot = 0
c_tot = 0

def nutrition_dashboard(calorie_target, calories_consumed, p, f, c):
    calories_left = calorie_target - calories_consumed
    print(f"You have {calories_left} calories left.")
    print(f"Protein: {p}g | Fiber: {f}g | Carbs: {c}g | Calories Consumed: {calories_consumed}")



def log_nutrition(calories_consumed, p, f, c):
    print("---Log Nutrition---")
    input_cal = input("Enter calories consumed:")
    input_car = input("Enter carbs consumed:")
    input_prot = input("Enter protein consumed:")
    input_fib = input("Enter fiber consumed:")

    if input_cal.isdigit() and input_car.isdigit() and input_prot.isdigit() and input_fib.isdigit():
        calories_consumed += int(input_cal)
        p += int(input_prot)
        f += int(input_fib)
        c += int(input_car)
        print("Your nutrition has been logged successfully!")

    else:
        print("Error, Invalid input.")

    return calories_consumed, p, f, c



def food_recommendations(calories_consumed, p, f, c):
    cuisine_options = ', '.join(Meal_Plan.keys())

    print(f"Cuisine options are: {cuisine_options}")
    preference = input("Enter your choice:").capitalize()

    if preference in Meal_Plan:
        print(f"Generating your {preference} meal plan...")

        for time_day in ["Breakfast", "Lunch", "Dinner",]:
            meal = random.choice(Meal_Plan[preference][time_day])
            print(f"{time_day}: {meal['name']} ({meal['calories']} calories)" )

            calories_consumed += meal['calories']
            p += meal['protein']
            f += meal['fiber']
            c += meal['carbs']

            print("Your meal has been added to your daily count!")

    else:
        print(f" {preference} is not available")
    return calories_consumed, p, f, c
    



def food_score(user, calorie_target, calories_consumed):
    if calories_consumed <= calorie_target:
        points += 60
    else:
        points -= 20
        
    user.set_food_score(points)


while True:
    print("choose from the selection list:")
    print("1. Cuisine selection")
    print("2. Log nutrition")
    print("3. Nutrition Dashboard")
    print("4. Exit")

    user_choice = input("Select from (1-4):")

    if user_choice == "1":
        calories_consumed, p_tot, f_tot, c_tot = food_recommendations(calories_consumed, p_tot, f_tot, c_tot)


    elif user_choice == "2":
        calories_consumed, p_tot, f_tot, c_tot = log_nutrition(calories_consumed, p_tot, f_tot, c_tot)


    elif user_choice == "3":
        nutrition_dashboard(calorie_target, calories_consumed, p_tot, f_tot, c_tot)


    elif user_choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose between 1, 2, 3, 4.")


    


        

    


        








    