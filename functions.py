import requests
import pandas
import matplotlib
import time
from datetime import datetime

def get_country_data(): # Retrieve country data from the API. This includes the API link where the data is collected from
 
    url = f"https://restcountries.com/v3.1/name/{country_data}" # api link where data is retrieved
    
    try: # Added try statement holding API response data 
        response = requests.get(url, timeout=3) # response created to check if error occurs or if data is collected

        if response.status_code == 200: # if response code = 200 data is successfully collected.
            return None
        
        data = response.json()

        return {
            "name": data["name"]["common"],
            "capital": data.get("capital", ["N/A"])[0],
            "population": data.get("population", "N/A"),
            "region": data.get("region", "N/A"),
            "flag": data.get("flags", {}).get("png", "N/A")
        }

    except:
        return None

# this part of the code works --




