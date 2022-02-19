# Imports
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Constants
ORIGIN_CITY_IATA = "LON"

dataManager = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()

# Get Data from Sheet
sheet_data = dataManager.get_destination_data()

# Check for IATA Codes
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flightSearch.get_destination_code(row["city"])

    dataManager.destination_data = sheet_data
    dataManager.update_destination()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flightSearch.check_flights(ORIGIN_CITY_IATA, destination["iata"], from_time=tomorrow, to_time=six_month_from_today)

    if flight.price < destination["lowestPrice"]:
        notificationManager.send_sms(message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")
