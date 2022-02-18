# Imports
import pandas as pd
import smtplib
from datetime import datetime
from random import choice

# Constants
MY_EMAIL = ""
MY_PASSWORD = ""

# Globals
letters = ["letter_1", "letter_2", "letter_3"]
message_content = ""

# Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient="records")

# Check if today matches a birthday in the birthdays.csv
def check_birthday():
    date = datetime.utcnow().strftime("%d:%m:%y").split(":")
    today_day = int(date[0])
    today_month = int(date[1])

    for birthday in birthday_list:
        if int(birthday["day"]) == today_day and int(birthday["month"]) == today_month:
            letter(birthday["name"])
            send_letter(birthday["email"])

# Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def letter(name):
    global message_content

    letter_chosen = choice(letters)

    with open(f"./letter_templates/{letter_chosen}.txt", "r") as f:
        message_content = f.read().replace("[NAME]", name)

# Send the letter generated to that person's email address.
def send_letter(email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=message_content
        )



