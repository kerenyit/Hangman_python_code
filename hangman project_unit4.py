# Write an error checks function
"""This program will allow the user to check
if the INPUT he enterd is a valid one english charcter or not.

#pseudo

ask the user for a charcter
if the user enterd one charcter
    if it is in English
        make sure it is in lower case
        print the charcter
    if its no in English
        return an error "E2"
if the user enterd longer than one charcters
    THEN Check if all the charcters are in English
    if all the charcters are in English:
        return error "E1"
    ELSE
        return error "E3"

Keywords: if, else, and
indent:
end block:
variables: English, charcter, longer than one

user_charcters=  INPUT("guess_a_letter:" )
number_of_charcters = len(user_charcters)

if number_of_charcters == 1:
    if user_charcters in alphabet:
        user_char= user_charcters.lower()
        print(user_char)
    else:
        return "E2"
if number_of_charcters > 1:
    is user_charcters in alphabet
    if True:
        return "E1"
    else:
        return "E3"



START program
enter user INPUT
alphabet- variable of English charcters
if user enterd one charcter:
    compare the charcter to see if charcter is in English

check if user INPUT is a string in English
check if the lenth of the user INPUT is equual to one
if user input is in english and longer than one charcter:
    return "E1"
if user input is not in english and string lenth equal one:
    return "E2"
if user input is longer than one and their are charcters not in english:
    return "E3"
if user input is in english and string lenth is equal to one:
     turn user input into small cases
     print user input


"""


def error_check(guess_a_letter):
    lnth_user_inp = len(guess_a_letter)
    if (lnth_user_inp > 1) and guess_a_letter.isalpha():
        return "E1"
    elif (lnth_user_inp == 1) and guess_a_letter.isalpha() != True:
        return "E2"
    elif (lnth_user_inp > 1) and guess_a_letter.isalpha() != True:
        return "E3"
    else:  # char input is correct
        letter_guessed = guess_a_letter.lower()
        return letter_guessed


guess_a_letter = input("Guess a letter:")

print(error_check(guess_a_letter))

--------------------------


def error_check2(guess_a_letter):
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


guess_a_letter = input("Guess a letter:")

print(error_check2(guess_a_letter))
