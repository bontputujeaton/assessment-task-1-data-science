# put input prompts and print prompts here from functions.py
from functions import time # import everything from functions.py into main.py

def countryapp_menu():
    print("Welcome to the Country Data Generator!")
    print("In this application you can view data on any city in the world.")
   #time.sleep(5)
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

