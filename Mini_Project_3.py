import random

def not_in_word():
    global guess_count
    print(f"Sorry, '{letter}' is not in the word.")
    print("")
    letters.append(letter)
    guess_count -=1

def in_word():
    print(f"Good job! '{letter}' is in the word.")
    print("")
    for ch in range(len(word)):
        if word[ch] == letter:
            hidden_word[ch] = letter
    letters.append(letter)

def win_game():
    global word
    word = "".join(word)
    print(f"Congratulations! You guessed the word: {word}")

def lose_game():
    global word
    word = "".join(word)
    print(f"Game over! The word was: {word}")

word_list = ["horse","apple","train","helicopter","bus","water","galaxy"]
guess_count = 6
word = []
letters = []
hidden_word = []

random_word = random.choice(word_list)
for ch in random_word:
    word.append(ch)
for ch in random_word:
    hidden_word.append("_")

print("Welcome to Hangman!")
print("")

while True:
    short_word = " ".join(word)
    short_hidden = " ".join(hidden_word)

    if guess_count == 0:
        lose_game()
        break

    if short_word == short_hidden:
        win_game()
        break
        
    print(f"Current word: {short_hidden}")
    print(f"Guessed letters: {letters}")
    print(f"Incorrect guesses remaining: {guess_count}")
    letter = input("Guess a letter:")

    if letter.isnumeric():
        print(f"{letter} is not a letter, try again")
        print("")
        continue

    if letter in letters:
        print(f"You already guess this letter, try again")
        print("")
        continue

    if letter in word:
        in_word()
        continue

    if letter not in word:
        not_in_word()
        continue