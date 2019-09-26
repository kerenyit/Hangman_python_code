
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


def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    if letter_guessed == "E1" or letter_guessed == "E3" or letter_guessed == "E2":
        old_letters_guessed = sorted(old_letters_guessed)
        old_letters_guessed = '->'.join(old_letters_guessed)
        print('X')
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
            print('X')
            print(old_letters_guessed)
            return False


def main():

    old_letters = ['a', 'c', 'p', 'e']
    check_update = try_update_letter_guessed(error_check(input("Guess a letter:")), old_letters)
    print(check_update)
    check_update = try_update_letter_guessed(error_check(input("Guess a letter:")), old_letters)
    print(check_update)
    print(old_letters)
    check_update = try_update_letter_guessed(error_check(input("Guess a letter:")), old_letters)
    print(check_update)
    check_update = try_update_letter_guessed(error_check(input("Guess a letter:")), old_letters)
    print(check_update)
    print(old_letters)


if __name__ == "__main__":
    main()
