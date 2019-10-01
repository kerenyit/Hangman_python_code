

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


def choose_a_word():
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
    chosen_word = count, w[i_count]
    secret_word = w[i_count]
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

    HANGMAN_PHOTOS = {0: image1, 1: image2, 2: image3, 3: image4, 4: image5, 5: image6, 6: image7}
    hangman_status = HANGMAN_PHOTOS[num_of_tries]
    return hangman_status


def guess_a_word(secret_word):
    """
    the function return the number of charcters in a words represened by a "_"
    """

    l_guess_word = len(secret_word)
    empty_char_word = "_ " * l_guess_word

    return secret_word, empty_char_word


def guess_a_letter():
    """
    the function return the charcter the user guessed
    """
    char = input("Guess a letter:")
    return char


def error_check(guess_a_letter):
    """
    pass
    """
    how_long = len(guess_a_letter)
    if (how_long > 1):
        if guess_a_letter.isalpha():
            return "E1"
        else:
            return "E3"
    elif (how_long == 1) and guess_a_letter.isalpha() != True:
        return "E2"
    else:  # char input is correct
        letter_guessed = guess_a_letter.lower()
        return letter_guessed


def check_valid_input(letter_guessed, old_letters_guessed):
    """# 5. ask the player to enter *1* character in English each round.
        #    - def guess_a_letter(): *this should be a while loop*
        # - 5.1. if the character isn't correct *or* was guessed before
        # print *"x"*, and the string of old_letters_guessed. and ask the
        # player to enter another character.
        #        - def error_check(guess_a_letter): *only* if its not in English
        #        and over one character *need to fix this*

        # - 5.2. if the  player enter *only one character is in English*
                # check if it is a correct guess or wrong one.
                # - def try_update_letter_guessed(letter_guessed, secret_word, old_letters_guessed):
                # *need to fix this code*"""
    lnth_user_inp = len(letter_guessed)
    if (lnth_user_inp > 1) or letter_guessed.isalpha() != True:
        print("x")
        return False
    elif letter_guessed in old_letters_guessed:
            #old_letters_guessed = old_letters_guessed.append(letter_guessed)
        print("x")
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    pass
    """
    wrong_guess = """\\    /
 \\  /
  \\/
  /\\
 /  \\
/    \\"""

    if letter_guessed == "E1" or letter_guessed == "E3" or letter_guessed == "E2":
        old_letters_guessed = sorted(old_letters_guessed)
        old_letters_guessed = '->'.join(old_letters_guessed)
        print(wrong_guess)
        print(old_letters_guessed)
        return False
    else:
        if letter_guessed not in old_letters_guessed:
            old_letters_guessed.append(letter_guessed)
            #old_letters_guessed = old_letters_guessed

            return True
        else:
            old_letters_guessed = sorted(old_letters_guessed)
            old_letters_guessed = '->'.join(old_letters_guessed)
            # old_letters
            print(wrong_guess)
            print(old_letters_guessed)
            return False


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
    length_of_secret_word = len(secret_word)

    string_of_secret_word = "_" * length_of_secret_word
    correct_letters = ""

    for char in secret_word:
        if char in old_letters_guessed:

            # print(char, "unchanged")
            correct_letters = correct_letters + char
        else:
            # print(char, "-->", new_char)
            position = secret_word.find(char)
            new_position = (position)
            new_char = string_of_secret_word[new_position]
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
        else:
            cnt = cnt
    if cnt == len(secret_word):
        return True
    else:
        return False


def main():
    Welcome_Screen()
    MAX_TRIES = 7
    secret_word, char_start = guess_a_word(choose_a_word())
    # choose_a_word()
    stat_p = 0
    start_point = print_hangman(stat_p)
    print(start_point)
    print(char_start)
    old_letters = list()
    while stat_p <= MAX_TRIES:
        char_guess = error_check(guess_a_letter())
        procces = try_update_letter_guessed(char_guess, old_letters)
        if procces == False:
            stat_p += 1
            print(print_hangman(stat_p))
            show_hidden_word(secret_word, old_letters)
        if procces == True:
            print(show_hidden_word(secret_word, old_letters))
            check_win(secret_word, old_letters)


if __name__ == "__main__":
    main()
