# Import all dependencies

# Requests for API handling

import requests 

# Pandas for data analysis

import pandas

# Matplotlib for visualisation (may not be needed in final product)

import matplotlib # may not need for my program

# Standard python time module

import time 

# More advanced than regular time module (also may not be needed in final product)

from datetime import datetime 

# Retrieve country data from the API. This includes the API link where the data is collected from

def get_countrydata(country_data): # Added country_data parameter inside

    # api link where data is retrieved

    url = f"https://restcountries.com/v3.1/name/{country_data}" 
    
    # Added try statement holding all API response data that is retrieved off user input. This is stored.

    try: 
        # response created to check if error occurs or if data is collected

        response = requests.get(url, timeout=3) 

        # if response code = 200 data is successfully collected.

        if response.status_code == 200: # Removed return None otherwise program would not run
            data = response.json()
            return { # Test #2 added [0] to each value so the API can return the list
                "name": data[0]["name"]["common"],
                "capital": data[0].get("capital", [""])[0],
                "population": data[0].get("population", ""),
                "continent": data[0].get("continents", [""])[0],
                "flag": data[0].get("flag", "")
        }
    
        return None # Test #3 Added return None if 200 response code is unsucessful (issue with program)

    except:
        return None


# Define show_dashboard function to display all the data stored from the API response to the user in a dashboard

def show_dashboard(data): # VISUALISATION
    name = data["name"] # extract name  
    capital = data["capital"] # extract capital
    population = data["population"] # extract population
    continent = data["continent"] # extact continent / region
    flag = data["flag"] # extract the country's flag as an emoji / icon
 
    # Population size label puts each country into a category depending on the amount of people
    if population >= 100_000_000: # If population is 100 million or more labelled as a large country
        size_label = "Large sized Country"
    elif population >= 10_000_000: #If population is 10 million or more labelled as a medium size country
        size_label = "Medium sized Country"
    else:
        size_label = "Small sized Country" # If population is 10 million or more labelled as a small country
 
    print("\n" + "=" * 50) # Print the border / divider line using '=' 
    print(f"  {flag}  COUNTRY DASHBOARD: {name.upper()}")
    print("=" * 50)
    print(f"  Capital City    : {capital}") # print capital city
    print(f"  Continent / Region  : {continent}") # print continent / region
    print(f"  Population : {population:,} ({size_label})") # print population
    print("=" * 50 + "\n") # Print the border / divider using = underneath at the bottom

# Save all the user's file data (information recieved from the API) to another file (country_history.txt)

def save_history(data): # Regulated wording of definition to match main file

    # Save the user's most recent data into a history data file that opens the file keeps existing content and adds new content to the end of the file

     with open("country_history.txt", "a") as country_datafile: # Use with instead of variable to ensure file is closed automatically and only open when saving

    # Convert population into a string file as the others are already strings and save other values into data file

        country_datafile.write(
            data["name"] + " " + 
            data["capital"] + " " + 
            str(data["population"]) + " " + 
            data["continent"] + "\n")

# View history of each country the user has inputted previously

# Another try statement implemented as the program would crash without it and view_countryhistory file can be created on the first user interaction with the program.

# "r" added to indicate file will be opened for reading by the user, new variable added ('as datafile')

def view_data_history(): 
    try:
        with open("country_history.txt", "r") as datafile: # open the file
            print("\nUser History:")
            print(datafile.read())
            print("\n")
    except:
        print("You don't have any countries currently saved.\n") # notifies the user if they haven't inputted any countries yet

    


        
      








