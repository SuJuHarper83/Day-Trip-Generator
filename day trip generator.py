# project: random trip generator

import random

# create function for each list below
destination = ["Paris", "London", "Chicago", "San Diego", "Austin", "Tokyo", "Melbourne", "Prague", "Costa Rica", "Tuscany"]
transportation = ["Tesla", "Ford", "Toyota", "moped", "horse drawn carriage", "taxicab", "Kia"]
restaurant = ["the Green Shamrock", "Ivory Coast", "the Sleepy Cat", "Night Shades", "the Black Stallion", "Bella Mia", "Sakura", "Moonshine", "Cicily"]
entertainment = ["dance at the South Seas", "sightsee", "go on a wine tasting trip", "visit the Museum of Fine Art", "go to the theater", "have a spa day", "tour the city", "visit the history museum", "go on a country bikeride"]

# generate random list item
def random_item_choice(list):
    random_item = random.choice(list)
    return random_item

print("Hello! I hear you are looking for ideas for your vacation. I would be happy to help you plan your trip! Let's try our trip generator! First, let's find out where you want to go! ")

def user_destination_choice():
    destination_choice = random_item_choice(destination)
    user_input = input(f"Would you like to to {destination_choice}? y/n ")
    if user_input == "n":
        return user_destination_choice()
    elif user_input == "y":
        print(f"Great! Thank you for confirming {destination_choice}! Let's now figure out how to get you there! ")
        return destination_choice

confirmed_destination = user_destination_choice()

print()

def user_transportation_choice():
    transportation_choice = random_item_choice(transportation)
    user_input = input(f"Would you like to take the {transportation_choice}? y/n ")
    if user_input == "n":
        return user_transportation_choice()
    elif user_input == "y":
        print(f"Fabulous! Thank you for confirming the {transportation_choice}. What restaurant would you like to visit while in town? ")
        return transportation_choice

confirmed_transportation = user_transportation_choice()

print() 

def user_restaurant_choice():
    restaurant_choice = random_item_choice(restaurant)
    user_input = input(f"Would you like to eat at {restaurant_choice}? y/n ")
    if user_input == "n":
        return user_restaurant_choice()
    elif user_input == "y":
        print(f"Perfect! Thank you for confirming {restaurant_choice}! Now let's figure out your ideal activity! ")
        return restaurant_choice

confirmed_restaurant = user_restaurant_choice()

print() 

def user_entertainment_choice():
    entertainment_choice = random_item_choice(entertainment)
    user_input = input(f"Would you like to {entertainment_choice}? y/n ")
    if user_input == "n":
        return user_entertainment_choice()
    elif user_input == "y":
        print(f"Fantastic! Thank you for confirming your choice to {entertainment_choice}! ")
        return entertainment_choice

confirmed_entertainment = user_entertainment_choice()

print()
print("Here is your trip as chosen by you: ")
print()
print(f"Destination: {confirmed_destination}")
print(f"Transportation: {confirmed_transportation}")
print(f"Restaurant: {confirmed_restaurant}")
print(f"Entertainment: {confirmed_entertainment}")
print()
print(f"You are on your way to {confirmed_destination}, via {confirmed_transportation}, with the chance to enjoy a wonderful dinner at {confirmed_restaurant} and the chance to {confirmed_entertainment}. Enjoy!! ")
