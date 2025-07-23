"""  Description: Play RPS against the computer. """

import random

def is_win(player, opponent):
    # Return True if player beats opponent
    return (
        (player == "r" and opponent == "s") or
        (player == "s" and opponent == "p") or
        (player == "p" and opponent == "r")
    )

def get_move_emoji(move):
    return {
        "r": "🪨 Rock",
        "p": "📄 Paper",
        "s": "✂️ Scissors"
    }.get(move, "❓")

def play():
    user = input("🎮 What's your choice? (r = 🪨, p = 📄, s = ✂️): ").lower()
    if user not in ['r', 'p', 's']:
        return "⚠️ Invalid input! Please choose 'r', 'p', or 's'."

    computer = random.choice(['r', 'p', 's'])

    user_move = get_move_emoji(user)
    computer_move = get_move_emoji(computer)

    print(f"🤖 Computer chose: {computer_move}")
    print(f"🧑 You chose: {user_move}")

    if user == computer:
        return "😐 It's a TIE!"

    if is_win(user, computer):
        return "🎉 You WON! 💪🔥"
    return "😞 You LOST... Better luck next time!"

# Game loop
play_again = "y"

print("🎮 Welcome to Rock, Paper, Scissors Game! ✊📄✂️\n")

while play_again == "y":
    print("\n--------------------------")
    print(play())
    print("--------------------------")
    play_again = input("\n🔁 Would you like to play again? (y/n): ").lower()
    while play_again not in ['y', 'n']:
        play_again = input("❓ Please enter 'y' to play again or 'n' to quit: ").lower()

print("\n🙏 Thanks for playing, warrior! See you next time. Jai Shri Ram 🚩")