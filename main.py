# put input prompts and print prompts here from functions.py
# Test run 4 import time module into main.py
import time
from functions import * 
# import everything from functions.py into main.py

def countryapp_menu():
    print("Welcome to the Country Data Generator!")
    print("In this application you can view data on any city in the world.")
    time.sleep(3)
    print("1. Search for a country's details")
    print("2. View the session history")
    print("3. Save session to the file")
    print("4. Get Help and Extra Information")
    print("5. Exit the program")  

def countryapp_help():
    print("USER HELP")
    time.sleep(0.3)
    print("Enter the name of any country to recieve its information. (#1)")
    time.sleep(0.3)
    print("You can view previous searches in 'View session history.' (#2)")
    time.sleep(0.3)
    print("Information about your chosen country includes name, capital city, population, region / continent, and flag.")
    time.sleep(0.3)
    print("Your input history (which countries you request data for) will be saved.")
    time.sleep(0.3)
    print("For any other option, type the menu number to choose it.")

while True:
    countryapp_menu()
    user_choice = input("What would you like to do?")

    if user_choice == "1":
        time.sleep(1)
        country = input("Enter the name of a country: ")
        
        data_result = get_countrydata(country.lower())

        if data_result:
            show_country(data_result) # this will be added as a function later
            save_history(data_result) # this will also be added as a function later
        else:
            print("Couldn't find the country. That might be an API error on our end? Please try again.")

    elif user_choice == "2":
        view_data_history() # function will be added later on to display data history to user

    elif user_choice == "3": # Bug testing fix - now saves instead of opening help menu by mistake

        ask_save_history = input("Are you sure you want to save your session? (y / n) ")
        if ask_save_history == "y":
            print("Your session has already been automatically saved after each search!")
        else:
            print("Returning to the main menu...")
        
    
    elif user_choice == "4":
        countryapp_help()

    elif user_choice == "5":
        confirm = input("Are you sure you want to exit the program? (y / n)")
        if confirm == 'y':
            print("Thank you for using the app! Application Made by Lumah Nyachhyon")
            break
        elif confirm == 'n':
            print("Loading you back to main menu...")
            time.sleep(3)
            
        else:
            print("Invalid option. Please select an option (1-5.)")
        