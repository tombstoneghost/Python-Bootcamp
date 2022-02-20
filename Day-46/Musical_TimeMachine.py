# Imports
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth

# CONSTANTS
BASE_URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = ""
CLIENT_SECRET = ""

# User Input
date_req = input("Which day would to like to travel? Type the date in YYYY-MM-DD format: ")


# Make Request to the URL
URL = BASE_URL + date_req
response = requests.get(URL)
website_html = response.text

# Beautiful Soup Object
soup = BeautifulSoup(website_html, "html.parser")

# Get the list
all_songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
songs = [song.find(name="h3", id="title-of-a-story").getText().strip() for song in all_songs]

# Login to Spotify
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", 
    redirect_uri="http://example.com", client_id=CLIENT_ID, client_secret=CLIENT_SECRET, show_dialog=True,cache_path="token.txt"))

user = spotify.current_user()["id"]

# Create Spotify Playlist
song_urls = []

year = date_req.split("-")[0]

for song in songs:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")

    try:
        url = result["tracks"]["items"][0]["url"]
        song_urls.append(url)
    except:
        print("f{song} does not exist on Spotify.")

playlist = spotify.user_playlist_create(user=user, name=f"Top-100-Billboard {date_req}", public=False)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_urls)

