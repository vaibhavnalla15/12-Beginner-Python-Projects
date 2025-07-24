import random
import string
from words import all_words  # Your words.py file must contain: all_words = [ "python", "hangman", ... ]

# ASCII Art for Hangman Stages
HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

# Function to choose a valid word
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

# Main game function
def hangman():
    word = get_valid_word(all_words)
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    print("🎮 Welcome to Hangman - Dynamic Edition!\n")

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show hangman art based on remaining lives
        print(HANGMAN_PICS[6 - lives])
        print(f"❤️ Lives left: {lives}")
        print(f"🔤 Used letters: {' '.join(sorted(used_letters))}")

        # Show current word progress
        current_word = [letter if letter in used_letters else '-' for letter in word]
        print("🧩 Word:", ' '.join(current_word))

        # Get input from user
        user_input = input("\n📥 Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)

            if user_input in word_letters:
                word_letters.remove(user_input)
                print("✅ Correct!")
            else:
                lives -= 1
                print("❌ Incorrect. You lose a life.")
        elif user_input in used_letters:
            print("⚠️ You already guessed that letter.")
        else:
            print("🚫 Invalid input. Please enter a letter from A-Z.")

    # Game end result
    if lives == 0:
        print(HANGMAN_PICS[-1])
        print(f"\n💀 You lost. The word was: {word}")
    else:
        print(f"\n🏆 Congratulations! You guessed the word: {word} 🎉")

# Start the game
hangman()
