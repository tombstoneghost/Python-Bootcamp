# Imports
import requests

# Constants
SHEETY_PRICES_ENDPOINT = ""
SHEETY_USERS_ENDPOINT = ""

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data
    
    def update_destination(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.post(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)

    def get_customer_emails(self):
        customer_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customer_endpoint)
        data = response.json()
        
        self.customer_data = data["users"]
        return self.customer_data

