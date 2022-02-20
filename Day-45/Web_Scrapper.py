# Imports
import requests
from bs4 import BeautifulSoup

# CONSTANTS
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Get Web Page Content
response = requests.get(url=URL)

website_html = response.text

# Make BeautifulSoup Object
soup = BeautifulSoup(website_html, "html.parser")

# Get all the movies
all_movies = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in all_movies][::-1]

# Save Data to a file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")





