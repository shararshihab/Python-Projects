import random
import string

from words_for_hangman import words


def get_valid_word(words):
    word = random.choice(words)    # randomly choose something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)   # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1   # takes away a life if wrong
                print("Letter is not in word.")

        elif user_letter in word_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # gets here when len(used_letters) == 0 OR when lives == 0
    if lives == 0:
        print(" ___________\n | /      |\n |/      ( )\n |       \ /\n |        |\n |       / \ \n_|__\nYou Died, sorry. Try Again!!\nThe word was", word, "!!")
    elif lives == 1:
        print(" ___________\n | /      |\n |/      ( )\n |       \ /\n |        |\n |\n_|__")
    elif lives == 2:
        print(" ___________\n | /      |\n |/      ( )\n |       \ /\n |        |\n |\n_|__")
    elif lives == 3:
        print(" ___________\n | /      |\n |/      ( )\n |       \ /\n |\n |\n_|__")
    elif lives == 4:
        print(" ___________\n | /      |\n |/      ( )\n |       \ \n |\n |\n_|__")
    elif lives == 5:
        print(" ___________\n | /      |\n |/      ( )\n |\n |\n |\n_|__")
    elif lives == 6:
        print(" ___________\n | /      |\n |/      (\n |\n |\n |\n_|__")
    elif lives == 7:
        print(" ___________\n | /      |\n |/\n |\n |\n |\n_|__")
    else:
        print("You guessed the word", word, "!!")

hangman()
