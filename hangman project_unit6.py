
"""write a function named def check_valid_input(letter_guessed, old_letters_guessed)
this FUNCTION GET:
letter_guessed = a STRING variable that the user just gussed
old_letters_guessed = a LIST variable with old gussed letters  the user
the FUNCTION return a boolean value that represent if the string is valid
and if it was gussed before.

the FUNCTION returns False if:
if the string is more than one charcter longer
if the string contain letters not in English/
if the string was already gussed and now he is in the LIST old_letters_guessed string/

the FUNCTION returns TRUE:
if the string is only one charcter in English and not in old_letters_guessed

Keywords: FUNCTION, GET, RETURN, FALSE, TRUE, IF,ELSE, LIST, STRING,VARIABLES

"""


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


def check_valid_input(letter_guessed, old_letters_guessed):
    if letter_guessed == "E1" or letter_guessed == "E3" or letter_guessed == "E2":
        return False
    else:
        if letter_guessed not in old_letters_guessed:
            old_letters_guessed = old_letters_guessed + [letter_guessed]
            return True
        else:
            return False


def main():
    guess_a_letter = input("Guess a letter:")
    letter_guessed = error_check(guess_a_letter)
    old_letters_guessed = []
    check_valid = check_valid_input(letter_guessed, old_letters_guessed)
    print(check_valid)


if __name__ == "__main__":
    main()
