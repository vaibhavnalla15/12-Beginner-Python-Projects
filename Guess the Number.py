""" Description: The computer tries to guess the number you’re thinking of. """
# Simple Method:-

import random

def guess(x):
    random_number = random.randint(1, x)
    User_guess = 0

    while User_guess != random_number:
        User_guess = int(input(f"Guess a number between 1 to {x}:- "))
        if User_guess < random_number:
            print("Sorry, Guess Again. Too Low")
        elif User_guess > random_number:
            print("Sorry, Guess Again. Too High")
    print(f"Yey, Congrats. You have Guessed the number {random_number} correctly. !!!")

guess(10)

# Advanced Method:-
from random import randint

EASY_MODE = 10
HARD_MODE = 5

# TODO 1:- Function to set difficulty
def level():
    Difficulty = input("Choose a difficulty. Type 'easy' or 'hard':- ").lower()
    if Difficulty == "easy":
        return EASY_MODE
    else:
        return HARD_MODE

# TODO 2:- Function to check users' guess against actual answer (user_guess, actual_answer, turns)
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"Hurray, You Got it !!! The answer is {actual_answer}")
        return None


# TODO 3:- Define Game
def game():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 to 100")
    answer = randint(1,100)
    turns = level()

# TODO 4:- Repeat the guessing functionality if they get it wrong. (guess = 0)
    user_guess = 0

# TODO 5:- Actual Loop
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        user_guess = int(input("Make a Guess:- "))
        # Track the number of turns and reduce by 1 if they get it wrong
        check_answer(user_guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, You Lose.")
            return
        elif user_guess != answer:
            print("Guess Again.")

game()