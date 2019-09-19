#check if input is valid

def is_valid_input(letter_guessed):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lnth_user_inp = len(letter_guessed)
    if (lnth_user_inp > 1):
        return False#, "the string is not a valid input"
    if letter_guessed not in alphabet:
        return False#, "the string is not a valid input"
    else:
        return True #, letter_guessed "is a valid input"

def main():
    is_valid =is_valid_input(input("Guess a letter:" ))
    print(is_valid)


if __name__ == "__main__":
    main()
