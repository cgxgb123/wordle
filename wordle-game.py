import random
words = ["QUEST", "TRUST", "FLASH", "QUICK", "JUICY", "ERODE", "GATOR", "GRAIL",
         "PRADA", "AAPEX"]
ANSWER = random.choice(words)
guesses = []  # Stores players guesses
status = ["#", "#", "#", "#", "#"]  # Keeps track of correct letters in correct positions
guess_count = 6  # Number of guesses the player has left
remaining_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # List of remaining letters from A to Z


print("Welcome to the Word Guessing Game!")
print("You have 6 attempts to guess the 5-letter word. Good luck!\n")

# Game Loop
while ANSWER != "".join(status) and guess_count > 0:
    # Display current game information
    print(f"Current Status: {''.join(status)}")
    print(f"Remaining Letters: {''.join(remaining_letters)}")
    
    # (a) Prompt the user for a guess
    guess = input("Enter a 5-letter word: ").upper()
    guesses.append(guess)

    # (b) Decrease the guess count
    guess_count -= 1
    
    # (c) Check if guess is of length 5
    if len(guess) == 5:
        print("Go you!")
        # Update remaining_letters based on guessed letters
        for letter in guess:
            if letter in remaining_letters:
                remaining_letters.remove(letter)
        
        # Check each letter in the guess against ANSWER
        for index, letter in enumerate(guess):
            if letter == ANSWER[index]:
                status[index] = letter
                print(f"Letter '{letter}' is in the correct position!")
            elif letter in ANSWER:
                print(f"Letter '{letter}' is in the word but in a different position.")
            else:
                print(f"Letter '{letter}' isn't in the word at all.")
    else:
        print("Error: Please enter exactly 5 letters.")

    # Display remaining guesses and current status
    print(f"\nGuesses left: {guess_count}")
    print(f"Updated Status: {''.join(status)}\n")

# End game message
if ANSWER == "".join(status):
    print(f"Congratulations! You've guessed the word '{ANSWER}' with {guess_count} guesses left!")
else:
    print("Out of guesses! Better luck next time!")
