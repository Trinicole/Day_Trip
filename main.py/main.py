import random

location_list = ["Canada", "South Korea", "Denmark", "Pananma"]
restaurant_list = ["Chik-fil-a", "Mcdonalds", "Texas Roadhouse", "Taco Bell"]
activity_list = ["Camping", "Horseback Riding", "Rock Climbing", "Cycling"]
transportation_list = ["Uber", "Train", "Bus", "Tram"]


def generate_ran_choice(list):
    random_selection = random.choice(list)
    user_validation = False
    while user_validation == False:
        random_selection = random.choice(list)
        user_input = input(f"Is this selection of {random_selection} okay?")
        if user_input == 'Yes': 
            print(f"Hope you enjoy {random_selection}")
            return random_selection
        else:
            print("We will select again for you!")

location = generate_ran_choice(location_list)
print(location)
restaurant = generate_ran_choice(restaurant_list)
print(restaurant)
activity = generate_ran_choice(activity_list)
print(activity)
transportation = generate_ran_choice(transportation_list)
print(transportation)













#def run_day_trip_generator(): 
#def generate_random_item(list_of_items): 
    #print(random.choice("location_list"))
    #print(random.choice("restaurant_list"))
    #print(random.choice("activity_list"))
    #print(random.choice("transportation_list"))
#def determine_satisfaction(current_trip, trip_options):
    #print("Are you satisfied with your trip? Yes or No")
    #Yes = print("Here is your final trip!")
    #No = print ("which option would you like to change? Location, Restaurant, Activity, Transsportation")
    #Location = print(random.choice("location_list"))
    #Activity = print(random.choice("activity_list"))
    #Transportation = print(random.choice("transportation_list"))