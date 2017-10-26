import requests
from random import choice
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com"


def start_game(quotes, num_guesses=4):
    quote = choice(quotes)
    print("Here's a quote: \n")
    print(quote['text'])
    guess = ''
    while guess != quote['author'] and num_guesses > 0:
        guess = input(f"\nWho said this? Guesses remaining: {num_guesses}. ")
        if guess == quote['author']:
            print("You guessed correctly! Congratulations!")
            break
        num_guesses -= 1
        if num_guesses == 3:
            response = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born in {birth_date} in {birth_place}.")
        elif num_guesses == 2:
            print(f"Here's a hint: The author's first name starts with {quote['author'].split(' ')[0][0]}")
        elif num_guesses == 1:
            print(f"Here's a hint: The author's last name starts with {quote['author'].split(' ')[-1][0]}")
        else:
            print(f"Sorry, you've run out of guesses. The answer was {quote['author']}\n")
    again = ''
    while again.lower() not in ('y', 'n', 'yes', 'no'):
        again = input("Would you like to play again (y/n)? ")
    if again.lower() in ('y', 'yes'):
        print("Great! Here we go again...\n")
        return start_game(quotes)
    else:
        print("Ok! See you next time!")
