# check if input is valid return boolean


def error_check(guess_a_letter):
    if (lnth_user_inp > 1) and (guess_a_letter in alphabet):
        return "E1"
    elif (lnth_user_inp == 1) and (guess_a_letter not in alphabet):
        return "E2"
    elif (lnth_user_inp > 1) and (guess_a_letter not in alphabet):
        return "E3"
    else:  # char input is correct
        guess_a_letter.lower()
        return guess_a_letter


def is_valid_input(letter_guessed):
    # return if the input string is more than one letters.
    if (lnth_user_inp > 1) or letter_guessed not in alphabet:
        return False  # , "the string is not a valid input"
    else:
        return True  # , letter_guessed "is a valid input"


def main():
    #global var
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    guess_a_letter = input("Guess a letter:")
    lnth_user_inp = len(letter_guessed)
    is_valid = is_valid_input(guess_a_letter)
    print(is_valid)


if __name__ == "__main__":
    main()
