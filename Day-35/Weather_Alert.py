# Imports
import requests
from twilio.rest import Client

# CONSTANTS
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
ACCOUNT_SID = ""
AUTH_TOKEN = ""

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body="It's going to rain today. Remember to bring an umbrella.", from_="", to="")
