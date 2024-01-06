import datetime
import requests
import spotipy
from bs4 import BeautifulSoup
from auth import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from spotipy.oauth2 import SpotifyOAuth


def validate(date_text):
    try:
        datetime.date.fromisoformat(date_text)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


target_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
validate(target_year)

# craft crawl URL
top_100_url = f"https://www.billboard.com/charts/hot-100/{target_year}/"

# crawl
response = requests.get(top_100_url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# filter for song titles, store in Python list
headline_tags = soup.select("li ul li h3")
headlines = [tag.getText().strip() for tag in headline_tags]

# create and fill Spotify Playlist
# connect to spotify
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=SPOTIFY_CLIENT_ID,
#         client_secret=SPOTIFY_CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="token.txt",
#         username="Freaky"
#     )
# )
# user_id = sp.current_user()["id"]


# store list in text file
counter = 1
with open("songs.txt", mode="w") as file:
    file.write(f"Top songs from {target_year}\n\n")
    for song in headlines:
        file.write(str(counter) + ". " + song + "\n")
        counter += 1