"""  Description: Play RPS against the computer. """

import random

def game():
    rps = ['r', 'p', 's']

    user_choice = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors:- ").lower()
    computer_choice = random.choice(rps)

    # If both player has choice
    if user_choice == computer_choice:
        print(f"Computer chose:-'{computer_choice}' Its a TIE.")

    # Check all the rules:-
    if user_choice == "p" and computer_choice == "r":
        print(f"Computer chose:-'{computer_choice}' You Win!!!")
    elif user_choice == "r" and computer_choice == "p":
        print(f"Computer chose:-'{computer_choice}' You Lost...")
    elif user_choice == "s" and computer_choice == "p":
        print(f"Computer chose:-'{computer_choice}' You Win!!!")
    elif user_choice == "p" and computer_choice == "s":
        print(f"Computer chose:-'{computer_choice}' You Lost...")
    elif user_choice == "r" and computer_choice == "s":
        print(f"Computer chose:-'{computer_choice}' You Win!!!")
    elif user_choice == "s" and computer_choice == "r":
        print(f"Computer chose:-'{computer_choice}' You Lost...")

game()