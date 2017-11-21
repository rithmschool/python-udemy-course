# Part 1: Text Exercise

For this exercise, we've provided you with some text from Alice's Adventures in Wonderland. Using this file as a testing ground, implement the following functions:

- `copy`: Takes in a file name and a new file name and copies the contents of the first file to the second file.

- `copy_and_reverse`: Takes in a file name and a new file name and copies the _reversed_ contents of the first file to the second file.

- `statistics`: Takes in a file name and returns a dictionary with the number of lines, words, and characters in the file.

- `find_and_replace`: Takes in a file name, a word to search for, and a replacement word. Replaces all instances of the word in the file with the replacement word.

# Part 2: CSV Exercise

For this exercise, you'll be working with a file called `users.csv`. Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following functions:

`print_user`: prints out all of the first and last names in the `users.csv` file

`add_user`: Takes in a first name and a last name and adds a new user to the `users.csv` file.

`find_user`: Takes in a first name and a last name and searches for a user with that first and last name in the `users.csv` file. If the user is found, `find_user`  returns the index where the user is found. Otherwise it returns a message stating that the user wasn't found.

`update_users`: Takes in an old first name, an old last name, a new first name, and a new last name. Updates the `users.csv` file so that any user whose first and last names match the old first and last names are updated to the new first and last names. The function should return a count of how many users were updated.

`delete_users`: Takes in a first name and a last name. Updates the `users.csv` file so that any user whose first and last names match the inputs are removed. The function should return a count of how many users were removed.