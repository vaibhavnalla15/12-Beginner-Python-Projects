""" Description: You try to guess the number the computer picked. """


import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f"Is {guess} too High (H), too Low (L), or Correct(C):- ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess}, correctly.")

computer_guess(1000)