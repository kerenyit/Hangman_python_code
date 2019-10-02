
def Welcome_Screen():
    """ This function print a Welcome Screen and the number of mistakes possible."""
    HANGMAN_ASCII_ART = """
          . ...          . .
  ...  .  .  . . ..   .  . .t8 8X..   .  . .  .. . .  .  .
...  .  .   .   .   .  .  . 8t@%.%.. .      .     .    .  ..
      . .    ..      . .    8:X8S@@ . . .  .  .  .  ..   .
  . .    ...     . .    ....@ tS @X  . . ..        .  ..  .
       .  . .  .     .  . .XS  % 8@t . ..   .  .     .  .
 .  .  .     .   .    . . 8t. %X:8 8 .    .. .   . .   . . .
  .  .  .  .  ..   ...  ..%S8.;;:t8  . .     .  .... .      
  ..  .   .      .:.  .   ;:88@8t.8t .   .    ...       .  .
 .  .   .    . ...  .    . % Xt;tt8@ .     . ... . .  .
     ..    .  ...   . . . S.8X.8@ XS . .  . ..    . .   . .
 . .    ..  .     .    . .:@:X88@%@X; . .  .  . .    .   .
      .   ..  .     .    ..XX  t%.%8:  ...        .   .:   .
  .  .  . . .   . .   .. . S8;X8X;:8:..   . .  .    . .  .
 .   ...     . .    ..   . t8::t.SS 8 .    . .   . .    .  .
  ....   .      . . .   . :%t8@::@S8 .  .     ..  .  .
  ... .    . .   ..   .  . t   %8 @S.     .  . ..      . .
...  . .      ..   ..     ..8;S:8t:; . .    .    . . .    ..
   .   . . . .   .    .. . S .@%;t88 .   . . .     .    . .
 .   .   . .   .     .  . t%.8X 8 S:t ... .    .  .  .. .
       . . . .    .    ...X%:%t  8X@%8S..  .    .    . . .
  . .   .    . .   .  ..  % @8 ...@S@;X:  . . .    ..     .
 .   . .   .  . .   ... 8@%;t .  . 88@: X..  .   ...   .  .
  ..     .       ....  @X@8..  . . .t:@;S. .  ....   .
 .  .. .    .  .... .. t.;8;   .  . . 8;.X; . .. .      . .
      .   .   ...   . 88SX%...     . .t8@.8X :.   .. .     .
 . .    .  . .    . . ;.;X:   . .    . SXt8@.   .    . . .
     .   ..    .     ;8.8  .      .   . %;X.t .    .  ..  .
  .    .  . .    . . St8;; ..  .   . .. X888;   .   . . .
 .  . ..     . .    .:X:8;;. .   . ... @; ;. ..   .    .  .
  . ... .  .    ..  : :;8X. . ..  ... %@ 88 . .  . . .     .
  ....    .  .    .. .%%@::%   .:...:%%8;SX .  ..       .
...  .  .     . .   . .;S:;t:SX8X%X%.%;8..   .   ..  .   . .
 .    . .  .  .   .   .. ;@:8.X8@;@8;SS% . .  .    .   . ..
   .     .  .   .       ..%;::.@:.88:8.

     """
    print(HANGMAN_ASCII_ART)
    MAX_TRIES = 7
    print(MAX_TRIES)


def choose_word():
    """
    This function ask the user to enter a file name and a number.
    then selects a word from a file_path by its index position
    :param file_path: file_path value
    :param index: index value
    :type file_path: str
    :type exponent: int
    :return: The result is the word that is in the index position
    :rtype: str
    """
    # check if the input is valid
    while True:
        try:
            file_path = input("Enter a file name:")
            fhand = open(file_path, 'r')
            break

        except:
            print("Something went wrong file", file_path)
            continue
        # check if the input is valid
    while True:
        try:
            index = input("Enter a number:")
            index = int(index)
            break
        except ValueError:
            print("ValueError index", index)
            continue
    count = 0
    lines = list()
    w = list()
    for line in fhand:
        words = line.split()
        for word in words:
            lines.append(word)
            if word not in w:
                count += 1
                w.append(word)
    fhand.close()
    i_count = index-1
    if index > count:
        i_count = (i_count) % len(lines)
    secret_word = w[i_count]
    print("Let's play!")
    return secret_word


def print_hangman(num_of_tries):
    """
    The function prints one of the seven states of the HANGMAN_PHOTOS,
    using a num_of_tries number that represents the number of failed
    attempts by the user so far.
    :param num_of_tries: num_of_tries value
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
    """
    The function calculate the length of the secret_word,
    and print a string of the same length in a underscore
    :param secret_word: secret_word value
    :type secret_word: string
    :return: None
    """

    length_secret_word = len(secret_word)
    temp_string_secret_word = "_ " * length_secret_word
    print(temp_string_secret_word)


def guess_a_letter():
    """
    The function shows the player a message asking him
    to type in a character (his guess), then enter the
    character into a variable and returns the character in lowcase
    """
    guessed_letter = input("Guess a letter in English:")
    guessed_letter = guessed_letter.lower()
    return guessed_letter


def check_valid_input(guessed_letter, old_letters_guessed):
    """
    The function calculate the length of the secret_word,
    and print a string of the same length in a underscore
    :param secret_word: secret_word value
    :type secret_word: string
    :return: None
    """
    if guessed_letter.isalpha() != True or len(guessed_letter) > 1:
        # print("X")
        return False
    elif guessed_letter in old_letters_guessed:
        # print("X")
        return False
    else:
        return True


def try_update_letter_guessed(guessed_letter, old_letters_guessed):
    """
    The function calculate the length of the secret_word,
    and print a string of the same length in a underscore
    :param secret_word: secret_word value
    :type secret_word: string
    :return: None
    """
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
    """
    The function calculate the length of the secret_word,
    and print a string of the same length in a underscore
    :param secret_word: secret_word value
    :type secret_word: string
    :return: None
    """
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
    MAX_TRIES = 1
    old_letters_guessed = list()
    secret_word = choose_word()
    num_of_tries = 1
    print_hangman(num_of_tries)
    empty_char(secret_word)
    while MAX_TRIES in range(7):
        guessed_letter = guess_a_letter()
        # check_valid_input(guessed_letter, old_letters_guessed)  # 5.2
        if try_update_letter_guessed(guessed_letter, old_letters_guessed) == True:
            if is_letter_in_secret_word(guessed_letter, secret_word) == False:
                MAX_TRIES += 1
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
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
