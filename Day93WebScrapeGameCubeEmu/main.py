import requests
import csv
from bs4 import BeautifulSoup

response = requests.get("https://wiki.dolphin-emu.org/index.php?title=Nintendo_GameCube")
response.raise_for_status()

website_source = response.text

soup = BeautifulSoup(website_source, "html.parser")

compatibility_table = soup.select_one('table.wikitable.sortable')
compatibility_list = []

if compatibility_table:
    for row in compatibility_table.find_all("tr"):
        columns = row.find_all("td")

        if len(columns) > 0:
            # easy, already gets string
            title = columns[0].get_text(strip=True)
            year = columns[1].get_text(strip=True)
            region = columns[2].get_text(strip=True)
            compatibility = columns[3].get_text(strip=True)

            compatibility_list.append(
                {
                    "Title": title,
                    "Year": year,
                    "Region": region,
                    "Compatibility": compatibility
                }
            )
else:
    raise Exception("No compatibility table found")

print(compatibility_list[0])

with open("compatibility_list.csv", "w", newline="") as csvfile:
    my_writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(compatibility_list[0].keys())

    row_content = [[row_dict["Title"], row_dict["Year"], row_dict["Region"], row_dict["Compatibility"]] for row_dict in
                   compatibility_list]
    my_writer.writerows(row_content)
