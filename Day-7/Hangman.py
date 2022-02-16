# Imports
import random
from Hangman_Art import stages, logo
from Hangman_Words import word_list


# Randomly choosing word from the list
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
word_length = len(chosen_word)

# End of Game
end_of_game = False

# Number of Lives
lives = 6

# Print Logo
print(logo)

while not end_of_game:
    # Asking User to guess a letter
    guess = input("Guess a letter: ").lower()

    # Checking the occurrence of the letter in chosen_word
    for i in range(0, word_length):
        if guess == chosen_word[i]:
            display[i] = guess

    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        
        
    print(' '.join(display))



    if '_' not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
