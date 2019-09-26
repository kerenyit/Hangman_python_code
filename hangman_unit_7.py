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
            position = secret_word.find(char)
            new_position = (position)
            new_char = string_of_secret_word[new_position]
            print(char, "unchanged")
            correct_letters = correct_letters + char
        else:
            print(char, "-->", new_char)
            correct_letters = correct_letters + new_char
    correct_letters = ' '.join(correct_letters)  # for usability there is an added space
    return correct_letters


secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']


print(show_hidden_word(secret_word, old_letters_guessed))
