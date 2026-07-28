import requests
from bs4 import BeautifulSoup

url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/7801/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

costs = soup.find("div", id="costs")

labels = costs.find_all("dt")
values = costs.find_all("dd")

for label, value in zip(labels, values):
    print("FIELD:", label.get_text(" ", strip=True))
    print("VALUE:", value.get_text(" ", strip=True))
    print("-----------------------------")