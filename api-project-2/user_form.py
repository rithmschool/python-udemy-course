import requests

print("---Please fill out this form below ---\n")

username, first_name, last_name, favorite_food = None, None, None, None

while not username:
    username = input("Enter a new username: ")
while not first_name:
    first_name = input("Enter your first name: ")
while not last_name:
    last_name = input("Enter your last name: ")

favorite_food = input("(Optional) Enter your favorite food: ")
post_body = {"username": username, "first_name": first_name, "last_name": last_name, "favorite_food": favorite_food}

response = requests.post('https://api.jsonbin.io/b', json=post_body, headers={"Content-Type": "application/json"})
response_json = response.json()

if response.status_code == 200:
    profile_id = response_json["id"]
    print(f"User profile created successfully. Your ID is {profile_id}")
else:
    print("API Error: ")
    print(response_json)
