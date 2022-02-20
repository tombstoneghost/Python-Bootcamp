# Imports
import requests
import smtplib
from bs4 import BeautifulSoup

# CONSTANTS
PRODUCT_URL = "https://www.amazon.in/Google-Pixel-Kinda-Coral-Storage/dp/B09LZ5G39D/ref=sr_1_1?keywords=pixel+6&qid=1645347654&sprefix=Pixel+6%2Caps%2C249&sr=8-1"
THRESHOLD_VALUE = 68000
SMTP_ADDRESS = ""
E_MAIL = ""
PASSWORD = ""


# Get the URL HTML
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
website_html = response.text

# Beautiful Soup Object
soup = BeautifulSoup(website_html, "html.parser")

prices = soup.find_all(name="span", class_="a-price")

price = int([price.find(name="span", class_="a-price-whole") for price in prices][0].getText().replace(",","").replace(".", ""))

# Send mail if the price is lower then threshold
product_name = soup.find(id="productTitle").get_text().strip()

if price < THRESHOLD_VALUE:
    message = f"{product_name} is now available at {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(E_MAIL, PASSWORD)
        connection.send_message(msg=message, from_addr=E_MAIL, to_addrs=E_MAIL)

