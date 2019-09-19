def check_valid_input(letter_guessed, old_letters_guessed):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    old_letters_guessed = ""

    lnth_letter_guessed = len(letter_guessed)
    if (lnth_letter_guessed > 1):
        return False  # , "the string is not a valid input"
    if letter_guessed not in alphabet:
        return False  # , "the string is not a valid input"
    if letter_guessed in old_letters_guessed:
        return False  # , "already gussed this letter"

    else:
        old_letters_guessed = old_letters_guessed + letter_guessed
        return True  # , letter_guessed "is a valid input"


def main():
    letter_guessed = check_valid_input(
        input("guess_a_letter:"), old_letters_guessed="")
    print(letter_guessed)


if __name__ == "__main__":
    main()
