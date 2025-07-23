"""  Description: Play RPS against the computer. """

import random

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    return (
            player == "r" and opponent == "s" or
            player == "s" and opponent == "p" or
            player == "p" and opponent == "r"
    )

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors:- ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f"Computer chose:-'{computer}' Its's TIE !!!"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return f"Computer chose:-'{computer}' You WON !!!"
    return f"Computer chose:-'{computer}' You LOST..."  # In this case we not added extra else statement to save line of code. like == if / else is_win(user, computer)....

print(play())
