import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

website_source = response.text

soup = BeautifulSoup(website_source, "html.parser")

articles = soup.select(".titleline a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_up_votes = [int(score.getText().split()[0]) for score in soup.select(".score")]

print(article_texts)
print(article_links)
print(article_up_votes)

# printing the triplet with the highest up votes
top_article_index = article_up_votes.index(max(article_up_votes))
print("Title: ", article_texts[top_article_index])
print("Link: ", article_links[top_article_index])
print("Up votes: ", article_up_votes[top_article_index])
