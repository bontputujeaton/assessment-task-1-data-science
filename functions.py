import requests
import pandas
import matplotlib
from datetime import datetime


country_data = input("Enter a country you would like to view information on: ") # enter country here prompt 

url = f"https://restcountries.com/v3.1/name/{country_data}" # api link where data is retrieved

response = requests.get(url) # response created to check if error occurs or if data is collected

if response.status_code == 200: # if response code = 200 data is successfully collected.
    data = response.json()

# this part of the code works
