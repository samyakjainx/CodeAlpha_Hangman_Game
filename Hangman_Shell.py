import random

def select_random_word():
    """Selects and returns a word from the predefined internship pool."""
    # Strict requirement: A small list of 5 predefined words [cite: 29]
    word_pool = ["PYTHON", "DEVELOPER", "GITHUB", "AUTOMATION", "SOFTWARE"]
    return random.choice(word_pool)

# Visual stages for the Hangman pole based on incorrect guesses (0 to 6)
HANGMAN_ART = [
    ["  +---+  ", "  |   |  ", "      |  ", "      |  ", "      |  ", "      |  ", "========="], 
    ["  +---+  ", "  |   |  ", "  O   |  ", "      |  ", "      |  ", "      |  ", "========="], 
    ["  +---+  ", "  |   |  ", "  O   |  ", "  |   |  ", "      |  ", "      |  ", "========="], 
    ["  +---+  ", "  |   |  ", "  O   |  ", " /|   |  ", "      |  ", "      |  ", "========="], 
    ["  +---+  ", "  |   |  ", "  O   |  ", " /|\\  |  ", "      |  ", "      |  ", "========="], 
    ["  +---+  ", "  |   |  ", "  O   |  ", " /|   |  ", " /    |  ", "      |  ", "========="], 
    ["  +---+  ", "  |   |  ", "  O   |  ", " /|\\  |  ", " / \\  |  ", "      |  ", "========="]  
]

def refresh_shell_layout(secret_word, guessed_letters, incorrect_guesses, message=""):
    """Prints a perfectly aligned interface box designed strictly for the IDLE Shell text engine."""
    # Small, controlled separation line to keep the game visually neat
    print("\n" + "-"*60 + "\n")
    
    max_attempts = 6 # Strict requirement limit [cite: 30]
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    history = ", ".join(sorted(guessed_letters)) if guessed_letters else "None"

    # Perfect Alignment Box (58 characters wide)
    print("+----------------------------------------------------------+")
    print("|              CODEALPHA HANGMAN CHAMPIONSHIP              |")
    print("+----------------------------------------------------------+")
    print(f"|  Secret Word:  {display_word.ljust(40)}  |")
    print(f"|  Strikes:      {f'{incorrect_guesses} / {max_attempts}'.ljust(40)}  |")
    print(f"|  Used Letters: {history.ljust(40)}  |")
    print("+----------------------------------------------------------+")
    print("|  CURRENT VISUAL STATUS:                                  |")
    
    art_frames = HANGMAN_ART[incorrect_guesses]
    for row in art_frames:
        print(f"|    {row.ljust(50)}    |")
        
    print("+----------------------------------------------------------+")
    
    if message:
        print(f"\n[*] Status: {message}")

def main():
    # Crucial: The word is picked ONCE when the program starts, ensuring it stays the same game!
    secret_word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    feedback_msg = "Game started. Guess a letter!"
    
    while incorrect_guesses < max_attempts:
        refresh_shell_layout(secret_word, guessed_letters, incorrect_guesses, feedback_msg)
        
        print() # Clean spacing for user prompt
        user_input = input(">> Enter your next guess (A-Z): ").strip().upper()
        
        if not user_input or len(user_input) != 1 or not user_input.isalpha():
            feedback_msg = "Invalid input: Please type exactly one alphabetic letter."
            continue
            
        if user_input in guessed_letters:
            feedback_msg = f"You already guessed '{user_input}'. Try another letter."
            continue
            
        guessed_letters.add(user_input)
        
        if user_input in secret_word:
            feedback_msg = f"Great guess! '{user_input}' is in the word."
            if all(char in guessed_letters for char in secret_word):
                refresh_shell_layout(secret_word, guessed_letters, incorrect_guesses, "Victory!")
                print("\n" + "="*58)
                print("🎉 CONGRATULATIONS! You successfully unlocked the word!")
                print(f"The word was indeed: {secret_word}")
                print("="*58)
                input("\nPress Enter to close the game...")
                return
        else:
            incorrect_guesses += 1
            feedback_msg = f"Oops! '{user_input}' is a strike."

    if incorrect_guesses == max_attempts:
        refresh_shell_layout(secret_word, guessed_letters, incorrect_guesses, "Game Over.")
        print("\n" + "="*58)
        print("💥 GAME OVER! You ran out of available attempts.")
        print(f"The correct word was: {secret_word}")
        print("="*58)
        input("\nPress Enter to close the game...")

if __name__ == "__main__":
    main()
