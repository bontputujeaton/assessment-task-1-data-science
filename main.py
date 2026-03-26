# put input prompts and print prompts here from functions.py
from functions import * 
# import everything from functions.py into main.py

def countryapp_menu():
    print("Welcome to the Country Data Generator!")
    print("In this application you can view data on any city in the world.")
    time.sleep(5)
    print("1. Search for a country's details")
    print("2. View the session history")
    print("3. Save session to the file")
    print("4. Get Help and Extra Information")
    print("5. Exit the program")  

def countryapp_help():
    print("USER HELP")
    print("Enter the name of any country to recieve its information. (#1)")
    print("You can view previous searches in 'View session history' (#2)")
    print("For any other option, type the menu number to choose it.")

while True:
    countryapp_menu()
    user_choice = input("What would you like to do?")

    if user_choice == "1":
        country = input("Enter the name of a country: ")
        
        data_result = get_country_data(country.lower())

        if data_result:
            show_country(data_result) # this will be added as a function later
            save_history(data_result) # this will also be added as a function later
        else:
            print("Couldn't find the country. That might be an API error on our end? Please try again.")

    
        