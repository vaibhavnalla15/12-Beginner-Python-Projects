""" Description: Guess a hidden word letter-by-letter before you lose all lives. """

import random
import string
from words import all_words  # Your words.py should contain a list called `all_words`


# Function to get a valid word (no hyphens or spaces)
def get_valid_word(words):
    word = random.choice(words)  # randomly pick a word
    while '-' in word or ' ' in word:
        word = random.choice(words)  # keep picking until it's a valid word
    return word.upper()  # convert to uppercase for consistency


# Main game function
def hangman():
    word = get_valid_word(all_words)  # get a word to guess
    word_letters = set(word)  # unique letters in the word
    alphabet = set(string.ascii_uppercase)  # all valid uppercase letters
    used_letters = set()  # letters guessed by the user
    lives = 6  # total number of chances

    print("🎮 Welcome to Hangman! Let's begin!\n")

    # Run the game until the word is guessed or user runs out of lives
    while len(word_letters) > 0 and lives > 0:
        # Show lives left and used letters so far
        print(f"\n❤️ You have {lives} lives left")
        print("🔤 Letters used:", " ".join(sorted(used_letters)))

        # Display current progress of the word
        word_display = [letter if letter in used_letters else "-" for letter in word]
        print("🧩 Current word:", " ".join(word_display))

        # Ask user for a letter input
        user_letter = input("📥 Guess a letter: ").upper()

        # Check if it's a new, valid guess
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # add to used letters

            if user_letter in word_letters:
                word_letters.remove(user_letter)  # correct guess
                print("✅ Good guess!")
            else:
                lives -= 1  # wrong guess, lose a life
                print("❌ Letter not in word.")

        # Already guessed
        elif user_letter in used_letters:
            print("⚠️ You already used that letter. Try a new one.")

        # Invalid input (not a letter)
        else:
            print("🚫 Invalid input. Please enter a letter.")

    # Game end conditions
    if lives == 0:
        print(f"\n💀 You died. The word was: {word}")
    else:
        print(f"\n🎉 Congrats! You guessed the word: {word} 🏆")


# Call the game
hangman()

