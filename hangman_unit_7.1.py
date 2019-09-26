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


secret_word = "friends"
old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
check_win(secret_word, old_letters_guessed)
secret_word = "yes"
old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
check_win(secret_word, old_letters_guessed)
