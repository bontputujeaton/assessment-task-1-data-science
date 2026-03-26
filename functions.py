import requests
import pandas
import matplotlib
import time
from datetime import datetime

def get_countrydata(): # Retrieve country data from the API. This includes the API link where the data is collected from
 
    url = f"https://restcountries.com/v3.1/name/{country_data}" # api link where data is retrieved
    
    try: # Added try statement holding all API response data that is retrieved off user input. This is stored.
        response = requests.get(url, timeout=3) # response created to check if error occurs or if data is collected

        if response.status_code == 200: # if response code = 200 data is successfully collected.
            return None
        
        data = response.json()

        return {
            "name": data["name"]["common"],
            "capital": data.get("capital", [""])[0],
            "population": data.get("population", ""),
            "region": data.get("region", ""),
            "flag": data.get("flags", {}).get("png", "")
        }

    except:
        return None
    
    
# Define display_country to display all the data stored from the API response to the user

def show_countrydata()






