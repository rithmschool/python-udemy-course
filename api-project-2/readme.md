# API Project Two

### Introduction

In this project, you will practice submitting form data as JSON to create an
online JSON document. You will implement two scripts:

1. A script that prompts the user from the command line and sends user data to
   [https://jsonbin.io](https://jsonbin.io), a free JSON storage service.
1. A script that retrieves the user profile using the ID generated from step 1.

### Requirements

1. Create a file called `user_form.py` which, when run, prompts the user for the
   following: `username`, `first_name`, `last_name`, `favorite_food`.
1. Make the first three fields required.
1. After `favorite_food` is entered, send a POST request to JSON Bin.
   * The POST request must be in JSON format
   * You can POST JSON using the `requests` module by passing
     `json=my_dictionary`, where `my_dictionary` is a Python dict containing the
     post data
   * For more information on how to POST to JSON Bin,
     [read the API reference here](https://jsonbin.io/api-reference).
1. The successful response will contain an automatically-generated unique ID
   attribute to reference later. You should print this ID when the script
   finishes.
   * If the response was not successful (i.e. if the server responds with
     something other than a **200** `status_code`., print an error message with
     the server response.
1. Make a second file called `fetch_profile.py` which, when run, prompts the
   user for a profile ID (the ID from step 4).
1. If the user enters a valid profile ID, print out the user profile.
   * If the response was not successful (i.e. if the server responds with
     something other than a **200** `status_code`., print an error message with
     the server response.

Good luck!
