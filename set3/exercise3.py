"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """


import random


def get_valid_integer_input(prompt):
    """Get a valid integer input from the user."""


while True:
    user_input = input(prompt)
    try:
        number = int(user_input)
        return number

    except ValueError:
        print("Invalid input. Please enter an integer value.")
    lower_bound = get_valid_integer_input("Enter the lower bound: ")
    upper_bound = get_valid_integer_input("Enter the upper bound: ")

    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound

    actual_number = random.randint(lower_bound, upper_bound)

    guessed = False

    while not guessed:
        guessedNumber = get_valid_integer_input(
            f"Guess a number between {lower_bound} and {upper_bound}: "
        )
    print(f"You guessed {guessedNumber},")

    if guessedNumber == actual_number:
        print(f"You got it!! It was {actual_number}")
        guessed = True
    elif guessedNumber < actual_number:
        print("Too small, try again :'(")
    else:
        print("Too big, try again :'(")
    return "You got it!"
