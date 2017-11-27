import requests

profile_id = None

while not profile_id:
    profile_id = input("Enter profile ID: ")

response = requests.get(f"https://api.jsonbin.io/b/{profile_id}")
response_json = response.json()

if response.status_code == 200:
    username = response_json["username"]
    first_name = response_json["first_name"]
    last_name = response_json["last_name"]
    favorite_food = response_json["favorite_food"]
    print("--- Below is your profile ---\n")
    print(f"Username: {username}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"favorite_food: {favorite_food}")
else:
    print("API Error: ")
    print(response_json)
