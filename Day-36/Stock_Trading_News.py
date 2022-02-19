# Imports
import requests
from twilio.rest import Client


# CONSTANTS
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

ACCOUNT_SID = ""
AUTH_TOKEN = ""


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# Get yesterday's closing price
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4. close"]


# Positive Difference between the closing prices
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price))

# Difference Percentage
diff_percentage = (difference / float(yesterday_closing_price)) * 100

# Check the Difference Percentage is greater than 5
if diff_percentage > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    for article in formatted_articles:
        message = client.messages.create(body=article, from_="", to="")
