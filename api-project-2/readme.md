# API Project Two

### Introduction

In this project, you will practice submitting data and storing an ID for later. You will implement a form-like prompt from the command line that sends user data to [https://jsonbin.io](https://jsonbin.io), a free JSON storage service, and then a script to retrieve the data for later.

### Requirements

1. Create a file called `user_form.py` which, when run, prompts the user for the following: `username`, `first_name`, `last_name`, `favorite_food`.
1. Make the first three fields required.
1. After submitting `favorite_food`, send a POST request to JSON Bin.
1. The response will contain a unique ID to reference later.
1. Make a second file called `fetch_profile.py` which, when run, prompts the user for a profile ID.
1. If the user enters a valid profile ID, print out the user profile.
1. Otherwise, print an error.

Good luck!