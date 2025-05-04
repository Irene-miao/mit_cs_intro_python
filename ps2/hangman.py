# Problem Set 2, hangman.py
# Name: Meow
# Collaborators:
# Time spent: 1 hour

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = ''
    print(letters_guessed)
    if len(letters_guessed) > 0 and len(secret_word) > 0:
       for l in letters_guessed:
           print(l)
           if l in secret_word:
               guess += l
    if len(secret_word) == len(guess):
       return True
    else:
       return False



def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    guess = ''
    if len(letters_guessed) > 0 and len(secret_word) > 0:
        for char in secret_word:
            if char in letters_guessed:
                if char not in guess:
                    guess += char
                else:
                    guess += '*'
    print(guess)
    return guess
    
    
    
    
    


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    not_guess = ''
    alphabet = string.ascii_lowercase
    print(alphabet)
    if len(letters_guessed) > 0:
        for char in alphabet:
            if char not in letters_guessed:
                not_guess += char
    print(not_guess)
    return not_guess



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 10
    letters_guessed = []
    available_letters = ''
    word_progress = ''
    
    while guesses > 0:
        vowels = 'aeiou'
        length = len(secret_word)
        guess = input(f'Hangman starts. The secret word has {length} characters. You have {guesses} guesses left.The letters not guessed: {available_letters}.The progress of the word : {word_progress}. Guess a letter:')
        if guess != '!' :
            if guess not in secret_word:
                letters_guessed.append(guess)
                
                if guess in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                    
            guesses -= 1
            available_letters = get_available_letters(letters_guessed)
            word_progress = get_word_progress(secret_word, letters_guessed)
            won = has_player_won(secret_word, letters_guessed)   
            if  won:
                print("You won!")
                break
       
        else:
            if guesses > 4:
                guesses -= 3
                word_progress = get_word_progress(secret_word, letters_guessed)
                for c in word_progress:
                    if c == '*':
                        index = word_progress.index(c)
                        letter = secret_word[index]
                        print(f'One letter in the word is {letter}.')
                        letters_guessed.append(letter)
                        continue
        

    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

     secret_word = choose_word(wordlist)
     with_help = False
     hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    #pass

