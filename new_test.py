
def Welcome_Screen():
    """Print a welcome message and number of attempts."""

    HANGMAN_ASCII_ART = """        _    _
       | |  | |
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                           __/  |
                          |____ / """

    print(HANGMAN_ASCII_ART)
    MAX_TRIES = 7
    print(MAX_TRIES)


def choose_word():
    """Choose a word from user input text file.

    This function ask the user to enter a file name and a number.
    It uses the try/except statement to check if the user enterd
    a valid input. If not it print a message on the screen, and ask
    the user to enter it again.
    When the input is correct it assignd to a variable fhand and index.
    It iterates over the lines of the file and selects a word in
    the position of given index.
    This function ask the user to enter a file name and a number.
    then selects a word from a file_path by its index position
    :return: The result is a word from the file in the place of the index.
    :rtype: str
    """
    while True:  # check if user input correct
        try:
            file_path = input("Enter a file name:")
            fhand = open(file_path, 'r')
            break

        except:
            print("I'm sorry,", "'", file_path, "'", "is not a corret file name. Please try again!")
            continue

    while True:  # check if user input correct
        try:
            index = input("Enter a number:")
            index = int(index)
            break
        except ValueError:
            print("I'm sorry,", "'", index, "'",  "is not a number. Please try again!")
            continue
    count = 0
    lines_l = list()
    words_l = list()
    for line in fhand:
        words = line.split()
        for word in words:
            lines_l.append(word)
            if word not in words_l:
                count += 1
                words_l.append(word)
    fhand.close()
    i_count = index-1
    if index > count:
        i_count = (i_count) % len(lines_l)  # circular count
    secret_word = words_l[i_count]
    print("Getting started...let's play!")
    return secret_word


def print_hangman(num_of_tries):
    """Prints the value from dict(HANGMAN_PHOTOS).

    This function gets the key- num_of_tries and print back it value.

    :param num_of_tries: num_of_tries is a key for dict(HANGMAN_PHOTOS)
    :type num_of_tries: int
    :return: None
    """

    HANGMAN_PHOTOS = {
        1: """    x-------x""",
        2: """    x-------x
    |
    |
    |
    |
    |""",
        3: """    x-------x
    |       |
    |       0
    |
    |
    |""",
        4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
        5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
        6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
        7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
    }
    hangman_status = HANGMAN_PHOTOS[num_of_tries]
    print(hangman_status)


def empty_char(secret_word):
    """Print the len(secret_word) using string of "_".

    The function calculate the length of the secret_word,
    and returns a 'blank' string of the same length using "_"
    :param secret_word: secret_word value.
    :type secret_word: str
    :return: A blank_secret_word
    :rtype: str
    """

    length_secret_word = len(secret_word)
    blank_secret_word = "_ " * length_secret_word
    return blank_secret_word


def guess_a_letter():
    """Ask the user to enter a letter.

    The function shows the player a message asking him to type in
    a character (his guess), then enter the character into a
    variable and returns the character in lowercase.
    :return: A character guessed_letter
    :rtype: str
    """

    guessed_letter = input("Guess a letter in English:")
    guessed_letter = guessed_letter.lower()
    return guessed_letter


def check_valid_input(guessed_letter, old_letters_guessed):
    """Check if the input in English and only 1 character long

    :param guessed_letter:A charcter value `guessed_letter`
    :type guessed_letter: str
    :param old_letters_guessed: old_letters_guessed value.
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool
    """
    if guessed_letter.isalpha() != True or len(guessed_letter) > 1:
        return False
    elif guessed_letter in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(guessed_letter, old_letters_guessed):
    """The function update old_letters_guessed list .

    This function uses the function check_valid_input() to update
    the character in old_letters_guessed list. If it false print
    a "X" to the user and also print a sorted string of
    old_letters_guessed list.
    :param guessed_letter: A charcter value `guessed_letter`
    :type guessed_letter: str
    :param old_letters_guessed: old_letters_guessed value.
    :type old_letters_guessed: list
    :return: returns False if it already exist or if check_valid_input is False, else returns True.
    :rtype: bool
    """

    if check_valid_input(guessed_letter, old_letters_guessed) == False:
        old_letters_guessed = sorted(old_letters_guessed)
        old_letters_guessed = '->'.join(old_letters_guessed)
        print('X')
        print(old_letters_guessed)
        return False
    else:
        old_letters_guessed.append(guessed_letter)
        return True


def is_letter_in_secret_word(guessed_letter, secret_word):
    """Check if guessed_letter in secret_word.

    :param guessed_letter:A charcter value `guessed_letter`.
    :type guessed_letter: str
    :param secret_word: A word that the user try to guess `secret_word`.
    :type secret_word: str
    :return: returns False if charcter value is not in secret_word, else returns True.
    :rtype: type
    """
    if guessed_letter not in secret_word:
        print(":(")
        return False
    else:
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    """ show correct letters outline of secret_word.

    If the guess was correct, replace "_" index  withh the correct letter of the secret_word.
    :param secret_word: A word that the user try to guess `secret_word`.
    :type secret_word: str
    :param old_letters_guessed: List containing all the letter the user already tried to guss `old_letters_guessed`.
    :type old_letters_guessed: str
    :return: The letters that was guessed and '_' string combind together and return both as a new it as a new correct_letters string.
    :rtype: str
    """

    length_secret_word = len(secret_word)
    string_secret_word = "_" * length_secret_word
    correct_letters = ""

    for char in secret_word:
        if char in old_letters_guessed:
            correct_letters = correct_letters + char
        else:
            position = secret_word.find(char)
            new_position = (position)
            # assign the char to the correct position in the emty string
            new_char = string_secret_word[new_position]
            correct_letters = correct_letters + new_char
    correct_letters = ' '.join(correct_letters)  # for usability this add a single space.
    return correct_letters


def check_win(secret_word, old_letters_guessed):
    """Short summary.

    :param secret_word: The word that the user try to guess `secret_word`
    :type secret_word: str
    :param old_letters_guessed: List containing all the letter the user already tried to guess `old_letters_guessed`.
    :type old_letters_guessed: list
    :return: TRUE if all the letters guessed by the user is in the secret_word, else return false.
    :rtype: bool
    """
    cnt = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            cnt = cnt+1
    if cnt == len(secret_word):
        return True
    else:
        return False


def main():
    Welcome_Screen()
    wrong_guess = 1
    num_of_tries = 1
    old_letters_guessed = list()  # create an empty list for the beginning
    secret_word = choose_word()
    print_hangman(num_of_tries)
    empty_char(secret_word)
    while wrong_guess in range(7):
        guessed_letter = guess_a_letter()
        if try_update_letter_guessed(guessed_letter, old_letters_guessed) == True:
            if is_letter_in_secret_word(guessed_letter, secret_word) == False:
                wrong_guess += 1
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print(show_hidden_word(secret_word, old_letters_guessed))
                if check_win(secret_word, old_letters_guessed) == True:
                    print("WIN")
                    break
    if wrong_guess == 7:
        if check_win(secret_word, old_letters_guessed) == True:
            print("WIN")
        else:
            print("LOSE")


if __name__ == "__main__":
    main()
