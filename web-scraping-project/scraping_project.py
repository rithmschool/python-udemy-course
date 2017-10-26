import requests
from bs4 import BeautifulSoup
from guessing_game import start_game, BASE_URL

url = "/page/1"
all_quotes = []

while url:
    response = requests.get(f"{BASE_URL}{url}")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
        })
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None

start_game(all_quotes)
