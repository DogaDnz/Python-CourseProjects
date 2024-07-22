import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
end_of_game = False
from hangman_words import word_list
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
    display += "_"

print(display)
print(stages[0])

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
        continue

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter
    else:
        lives -= 1
        print(stages[6 - lives])
        print(f"You guessed {guess} thats not in the word, You lose a life.")
        if lives == 0:
            end_of_game = True
            print("Game Over. You lost.")
            print(f"The correct word was: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
