import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_data = []

for book in books:
    title = book.find("h3").find("a")["title"]

    price = book.find("p", class_="price_color").text

    rating = book.find("p")["class"][1]

    book_data.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

# Convert data into a table
df = pd.DataFrame(book_data)

# Save as CSV
df.to_csv("books.csv", index=False)

print("Scraping completed! Data saved to books.csv")