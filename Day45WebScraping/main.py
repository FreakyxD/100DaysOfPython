from bs4 import BeautifulSoup

with open("website.html") as file:
    website_content = file.read()

soup = BeautifulSoup(website_content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")  # css selector
print(company_url)

headings = soup.select(selector=".heading")
print(headings)
