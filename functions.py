import requests

country_data = input("Enter a country you would like to view information on: ")

url = f"https://restcountries.com/v3.1/name/{country_data}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()