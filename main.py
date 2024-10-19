import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

SHEETY_ENDPOINT =  "https://api.sheety.co/c6583818d10ceba595ae749cfc283c9b/myWorkouts/workouts"
NUTRI_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

#ENV variables
NUTRI_APPLICATION_ID = os.getenv("NUTRI_APPLICATION_ID")
NUTRI_API_KEY = os.getenv("NUTRI_API_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")


#Format current date and time
now = datetime.now()
current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

#user input
query = input("Tell me which exercises you did: \n")

#Process data on Nutritionix
nutritionix_headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRI_APPLICATION_ID,
    "x-app-key": NUTRI_API_KEY
}
nutri_parameters = {
    "query": query
}

try:
    response = requests.post(NUTRI_URL, json=nutri_parameters, headers=nutritionix_headers)
    response.raise_for_status()
    exercises = response.json()["exercises"]
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Nutritionix API: {e}")
    exercises = []


#Add data to spreadsheet using Sheety
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_TOKEN
}

#separate workouts in different rows
for exercise in exercises:
    sheety_parameters = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    try:
        response = requests.post(SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
        response.raise_for_status()  # Ensure request was successful
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error posting data to Sheety API: {e}")