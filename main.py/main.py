import random

def run_day_trip_generator(): 

 def print_full_trip(list_of_options): 
    location_list = ["Canada", "South Korea", "Denmark", "Pananma"]
    restaurant_list = ["Chik-fil-a", "Mcdonalds", "Texas Roadhouse", "Taco Bell"]
    activity_list = ["Camping", "Horseback Riding","Rock Climbing", "Cycling"]
    transportation_list = ["Uber", "Train", "Bus", "Tram"]
def generate_random_item(list_of_items): 
    print(random.choice("location_list"))
    print(random.choice("restaurant_list"))
    print(random.choice("activity_list"))
    print(random.choice("transportation_list"))
def determine_satisfaction(current_trip, trip_options):
    print("Are you satisfied with your trip? Yes or No")
    Yes = print("Here is your final trip!")
    No = print ("which option would you like to change? Location, Restaurant, Activity, Transsportation")
    Location = print(random.choice("location_list"))
    Restaurant = print(random.choice("restaurant_list"))
    Activity = print(random.choice("activity_list"))
    Transportation = print(random.choice("transportation_list"))