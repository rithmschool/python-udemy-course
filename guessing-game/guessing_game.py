import random

random_number = random.randint(0, 9) + 1  # numbers 1 - 10

while True:
    # get user guess and make it an integer
    user_guess = input("Guess a number between 1 and 10: ")
    user_guess = int(user_guess)

    if user_guess > random_number:
        print("Too high, try again!")
    elif user_guess < random_number:
        print("Too low, try again!")
    elif user_guess == random_number:
        print("You guessed it! You won!")
        play_again = input("Do you want to keep playing? (y/n) ")
        if play_again == "y":
            # new random number
            random_number = random.randint(0, 9) + 1
            user_guess = None
        else:
            print("Thanks for playing. Bye!")
            break
