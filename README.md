Word Guessing Game
A VERY simple (can't emphasize the simplicity enough) word-guessing game implemented in Python. The player has six attempts to guess a randomly selected 5-letter word. Feedback is provided for each guess, indicating which letters are in the correct position, which letters are in the word but in a different position, and which letters are not in the word at all.

How to Play
The program randomly selects a 5-letter word from a predefined list of words.
You have 6 attempts to guess the correct word.
After each guess, the game provides feedback:
Letters that are in the correct position are revealed.
Letters that are in the word but not in the correct position are noted.
Letters that aren't in the word at all are also specified.

Game Rules
Each guess must be exactly 5 letters.
You can use uppercase or lowercase letters (the program converts input to uppercase).
The game will track letters you've already guessed, making it easier to narrow down your options.
If you correctly guess the word within six attempts, you win the game. Otherwise, the game will reveal the correct word.

Features
Tracks and displays which letters have been guessed already.
Provides feedback after each guess to help narrow down the word.
Simple terminal interface with clear prompts and feedback.



Example Output
plaintext
Copy code
Welcome to the Word Guessing Game!
You have 6 attempts to guess the 5-letter word. Good luck!

Current Status: #####
Remaining Letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Enter a 5-letter word: FLASH
Go you!
Letter 'F' isn't in the word at all.
Letter 'L' is in the word but in a different position.
Letter 'A' isn't in the word at all.
Letter 'S' is in the correct position!
Letter 'H' isn't in the word at all.

Guesses left: 5
Updated Status: #S###

...
Code Overview
words: A list of potential words that the game can randomly select from.
ANSWER: The selected answer for the current game session.
guesses: A list to store each guess made by the player.
status: A list that keeps track of the current state of the correctly guessed letters in their positions.
guess_count: Tracks the number of guesses the player has left.
remaining_letters: Displays the letters that haven’t been guessed yet to help the player.
License
This project is open-source and available for educational purposes. Feel free to modify and experiment with it.

This README file should help users understand and run the game easily. Let me know if you need more details added!
