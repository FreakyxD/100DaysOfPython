import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
movie_website_content = response.text

soup = BeautifulSoup(movie_website_content, features="html.parser")

tags = soup.find_all("h3", class_="title")
list_of_movies_desc = [tag.getText() for tag in tags]

list_of_movies_asc = list(reversed(list_of_movies_desc))

with open("BestMovies.txt", mode="w") as file:
    for movie in list_of_movies_asc:
        print(f"Adding line: {movie}")
        file.write(f"{movie}\n")
                        