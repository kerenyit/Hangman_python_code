#Write an error checks function

def error_check(guess_a_letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lnth_user_inp = len(guess_a_letter)
    if (lnth_user_inp > 1) and (guess_a_letter in alphabet):
        return "E1"
    elif (lnth_user_inp == 1) and (guess_a_letter not in alphabet):
        return "E2"
    elif (lnth_user_inp > 1) and (guess_a_letter not in alphabet):
        return "E3"
    else: #char input is correct
        guess_a_letter.lower()
        return guess_a_letter


guess_a_letter= input("Guess a letter:" )

print(error_check(guess_a_letter))
