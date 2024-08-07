import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

stages = ['''
  +---+
  |   |
  O   |
 /|/  |
 / /  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|/  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|/  |
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

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

PH = ""
while PH != chosen_word:
    if lives == 0:
        print("You loose.")
        break

    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            PH = "".join(display)
    if guess not in chosen_word:
        lives -= 1

    print(display)
    print(stages[lives])

    if lives > 0 and PH == chosen_word:
        print("You win!")

