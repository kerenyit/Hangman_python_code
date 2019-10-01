# hangman_game works as required


def Welcome_Screen():
    """
    this FUNCTION will print a  Welcome Screen, and the number of mistakes possible.
    PARAM:
    HANGMAN_ASCII_ART= STRING that represent a logo.
    MAX_TRIES= int that represent possible mistakes
    the FUNCTION print the PARAM:
     """
    HANGMAN_ASCII_ART = """  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/  |
                    |____ / """
    print(HANGMAN_ASCII_ART)

    # limit gusses by using randint function
    MAX_TRIES = 7
    print(MAX_TRIES)


def choose_word():
    """
    this FUNCTION  ask the user to choose a text file, and an index
    to create the secret word he user will need to guess
    PARAM:
    HANGMAN_ASCII_ART= STRING that represent a logo.
    the FUNCTION print the PARAM:
     """
    fname = input("Enter a file name:")
    index = int(input("enter a number:"))
    fhand = open(fname, 'r')
    count = 0
    text_l = list()
    w = list()
    for line in fhand:
        words = line.split()
        for word in words:
            text_l.append(word)
            if word not in w:
                count += 1
                w.append(word)
    fhand.close()
    i_count = index-1
    if index > count:
        i_count = (i_count) % len(text_l)
        # print(i_count)
    # chosen_word = count, w[i_count]
    secret_word = w[i_count]
    print("Let's play!")
    return secret_word


def print_hangman(num_of_tries):
    """
    VARIABLE-  HANGMAN_PHOTOS (dict)- from unit 1
    the FUNCTION PRINT:
    one of the 7 photos in HANGMAN_PHOTOS-
    with the help of a VARIABLE-num_of_tries that represent
    how many times the user
    guessed the wrong letter, and  HANGMAN_PHOTOS
    dict[key] = value
    """
    # picture 1:
    image1 = "x-------x"
    # picture 2:
    image2 = """x-------x
|
|
|
|
|"""
    # picture 3:
    image3 = """x-------x
|       |
|       0
|
|
|"""
    # picture 4:
    image4 = """x-------x
|       |
|       0
|       |
|
|"""
    # picture 5:
    image5 = """x-------x
|       |
|       0
|      /|\\
|
|"""
    # picture 6:
    image6 = """x-------x
|       |
|       0
|      /|\\
|      /
|"""
    # picture 7:
    image7 = """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""

    HANGMAN_PHOTOS = {1: image1, 2: image2, 3: image3, 4: image4, 5: image5, 6: image6, 7: image7}
    hangman_status = HANGMAN_PHOTOS[num_of_tries]
    # return hangman_status
    print(hangman_status)


def empty_char(secret_word):

    # compute the length of the word
    length_secret_word = len(secret_word)
    temp_string_secret_word = "_ " * length_secret_word

# print an image of empty position based on the length of the word
    print(temp_string_secret_word)


def guess_a_letter():
    guessed_letter = input("Guess a letter:")
    guessed_letter = guessed_letter.lower()
    return guessed_letter


def check_valid_input(guessed_letter, old_letters_guessed):
    if guessed_letter.isalpha() != True or len(guessed_letter) > 1:
        # print("X")
        return False
    elif guessed_letter in old_letters_guessed:
        # print("X")
        return False
    else:
        return True  # letter_guessed "is a valid input"


def try_update_letter_guessed(guessed_letter, old_letters_guessed):

    if check_valid_input(guessed_letter, old_letters_guessed) == False:
        old_letters_guessed = sorted(old_letters_guessed)
        old_letters_guessed = '->'.join(old_letters_guessed)
        print('X')
        print(old_letters_guessed)
        return False
    else:
        # letter_guessed not in old_letters_guessed:
        old_letters_guessed.append(guessed_letter)
        # old_letters_guessed = old_letters_guessed
        return True


def is_letter_in_secret_word(guessed_letter, secret_word):
    if guessed_letter not in secret_word:
        print(":(")
        return False
    else:
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    """the FUNCTION GET:
    secret_word= STRING for the user to guess_a_letter
    old_letters_guessed= LIST containing the letter the user already guessed/
    the FUNCTION RETURN:
    correct_letters= containing letters and '_'. the STRING SHOW the letters from
    the LIST old_letters_guessed that ar in thr right place of the STRING
    secret_word, and the letters the user haven't guessed yet with '_'

    instructions:

    usability-make it clear for the user- add spaces between '_' so that he can see how many letter
    he has'nt guessed yet.
    """
    length_secret_word = len(secret_word)

    string_secret_word = "_" * length_secret_word
    correct_letters = ""

    for char in secret_word:
        if char in old_letters_guessed:
            correct_letters = correct_letters + char
        else:  # char not in old_letters_guessed:
            position = secret_word.find(char)
            new_position = (position)
            new_char = string_secret_word[new_position]
            correct_letters = correct_letters + new_char
    correct_letters = ' '.join(correct_letters)  # for usability there is an added space
    return correct_letters


def check_win(secret_word, old_letters_guessed):
    """the FUNCTION GET:
    secret_word= STRING for the user to guess_a_letter
    old_letters_guessed= LIST containing the letter the user already guessed/
    the FUNCTION RETURN:
    TRUE= IF all the letters the user guessed is in the secret_word
        ELSE= FALSE

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
    Welcome_Screen()  # 1. first print a Welcome_Screen
    MAX_TRIES = 1
    old_letters_guessed = list()
    secret_word = choose_word()  # 2 . ask the player to enter a file and a number, return the secret_word
    num_of_tries = 1
    print_hangman(num_of_tries)  # 3
    empty_char(secret_word)  # 4
    while MAX_TRIES in range(7):  # 5
        guessed_letter = guess_a_letter()  # 5.1
        # check_valid_input(guessed_letter, old_letters_guessed)  # 5.2
        if try_update_letter_guessed(guessed_letter, old_letters_guessed) == True:
            if is_letter_in_secret_word(guessed_letter, secret_word) == False:  # 5.4.1
                MAX_TRIES += 1
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:  # MAX_TRIES == 7:
                print(show_hidden_word(secret_word, old_letters_guessed))
                if check_win(secret_word, old_letters_guessed) == True:
                    print("WIN")
                    break
    if MAX_TRIES == 7:
        if check_win(secret_word, old_letters_guessed) == True:
            print("WIN")
        else:
            print("LOSE")


if __name__ == "__main__":
    main()
