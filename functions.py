# Import all dependencies
import requests # Requests for API handling
import pandas # Pandas for data analysis
import matplotlib # Matplotlib for visualisation (may not be needed in final product)
import time # Standard python time module
from datetime import datetime # More advanced than regular time module (also may not be needed in final product)

# Retrieve country data from the API. This includes the API link where the data is collected from
def get_countrydata(): 
    # api link where data is retrieved
    url = f"https://restcountries.com/v3.1/name/{country_data}" 
    
    # Added try statement holding all API response data that is retrieved off user input. This is stored.
    try: 
        # response created to check if error occurs or if data is collected
        response = requests.get(url, timeout=3) 

        # if response code = 200 data is successfully collected.
        if response.status_code == 200: 
            return None
        

        data = response.json()

        return {
            "name": data["name"]["common"],
            "capital": data.get("capital", [""])[0],
            "population": data.get("population", ""),
            "region": data.get("region", ""),
            "flag": data.get("flag", {}).get("png", "")
        }

    except:
        return None


# Define display_country to display all the data stored from the API response to the user
def show_countrydata():
    print(f"\n Here's some information about", data["name"], ":")
    print("Country Name:", data["name"])
    time.sleep(0.5)
    print("Capital:", data["capital"])
    time.sleep(0.3)
    print("Population:", data["population"])
    time.sleep(0.3)
    print("Region:", data["region"])
    time.sleep(0.3)
    print("Flag:", data["flag"])
    time.sleep(0.1)
    print("\n")

# Save all the user's file data (information recieved from the API) to another file (country_history.txt)

def save_countrydata():
    with open


        
      








