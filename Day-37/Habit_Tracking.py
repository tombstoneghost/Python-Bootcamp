# Imports
from urllib import response
import requests
from datetime import datetime

# CONSTANTS
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = "test_user"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = ""
PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/"

# User Registration
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)


# Graph Generation
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers={
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)

# Add Data to Graph
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "9.74"
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)

# Update Data
UPDATE_ENDPOINT = UPDATE_ENDPOINT + today

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=UPDATE_ENDPOINT, json=new_pixel_data, headers=headers)

# Delete Data
DELETE_ENDPOINT = UPDATE_ENDPOINT

response = requests.put(url=DELETE_ENDPOINT, headers=headers)
