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

        return {
            "name": data["name"]["common"],
            "capital": data.get("capital", [""])[0],
            "population": data.get("population", ""),
            "continent": data.get("continent", ""),
            "flag": data.get("flag", {}).get("png", "")
        }

    except:
        return None


# Define display_country to display all the data stored from the API response to the user

def show_countrydata(data):

    print(f"\n Here's some information about", data["name"], ":")

    print("Country Name:", data["name"])

    time.sleep(0.5)

    print("Capital:", data["capital"])

    time.sleep(0.3)

    print("Population:", data["population"])

    time.sleep(0.3)

    print("Continent:", data["continent"])

    time.sleep(0.3)

    print("Flag:", data["flag"])

    time.sleep(0.1)

    print("\n")

# Save all the user's file data (information recieved from the API) to another file (country_history.txt)

def save_countrydata(data):

    # Save the user's most recent data into a history data file that opens the file keeps existing content and adds new content to the end of the file

    country_datafile = open("country_history.txt", "a")

    # Convert population into a string file as the others are already strings and save other values into data file

    country_datafile.write(data["name"] + " " + data["capital"] + " " + str(data["population"]) + " " + data["continent"] + "\n")

# View history of each country the user has inputted previously

def view_countryhistory():

    # Another try statement implemented as the program would crash without it and view_countryhistory file can be created on the first user interaction with the program.

    try:

        # "r" added to indicate file will be opened for reading by the user, new variable added ('as datafile')
        with open("country_history.txt", "r") as datafile:
            print("\nUser History:")
            print(datafile.read())
            print("\n")
    except:
        print("You don't have any countries currently saved.\n")

    


        
      








