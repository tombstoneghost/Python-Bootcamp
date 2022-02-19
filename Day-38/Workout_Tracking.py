# Imports
import re
import requests
from datetime import datetime

# CONSTANTS
APP_ID = ""
API_KEY = ""
SHEET_TOKEN = ""

GENDER = "Male"
WEIGHT_KG = 85
HEIGHT_CM = 175
AGE = 22

EXERCISE_INFORMATION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = ""


# Header
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# GET Exercise Stats
exercise = input("Which exercise you did: ")

exercise_params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=EXERCISE_INFORMATION_ENDPOINT, json=exercise_params, headers=headers)
data = response.json()

# Saving data to Google Sheets
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")


sheet_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}


for exercise in data["exercise"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_input, headers=sheet_headers)

