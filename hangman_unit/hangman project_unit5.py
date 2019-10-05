
def error_check(guess_a_letter):
    lnth_user_inp = len(guess_a_letter)
    if (lnth_user_inp > 1):
        if guess_a_letter.isalpha():
            return "E1"
        else:
            return "E3"
    elif (lnth_user_inp == 1) and guess_a_letter.isalpha() != True:
        return "E2"
    else:  # char input is correct
        letter_guessed = guess_a_letter.lower()
        return letter_guessed


def is_valid_input(letter_guessed):
    if letter_guessed == "E1" or letter_guessed == "E3" or letter_guessed == "E2":
        return False  # , "the string is not a valid input"
    else:
        return True  # , letter_guessed "is a valid input"


def main():
    guess_a_letter = input("Guess a letter:")
    error = error_check(guess_a_letter)
    is_valid = is_valid_input(error)
    print(is_valid)


if __name__ == "__main__":
    main()

"-------------------"
test1 = main()
test2 = main()
test3 = main()
test4 = main()
