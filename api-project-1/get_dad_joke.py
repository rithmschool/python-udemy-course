import requests
from random import choice

term = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": term}
).json()
results = response["results"]
total_jokes = response["total_jokes"]
if total_jokes > 1:
    print(
        f"I've got {total_jokes} jokes about {term}. Here's one:\n",
        f"{choice(results)['joke']}"
    )
elif total_jokes == 1:
    print(
        f"I've got one joke about {term}. Here it is:\n",
        f"{results[0]['joke']}"
    )
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")
