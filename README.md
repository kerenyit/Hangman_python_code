## **Hangmam**

This is the instruction for coding a game of  **Hangmam**  in *python*.

#Getting Started

1. first print a Welcome_Screen
    - def Welcome_Screen():with the name of the game and number of possible wrong answers.

2. ask the player to enter a file and a number:
    - def choose_a_word(): this will return the secret_word he will
    had to guess.

3. show the player his current status of the game.
    - def print_hangman(num_of_tries): according to his number of wrong guesses- in the beginning its the first one.

4. underneath the image of the hangman. show the status of the secret_word
   in blank lines.
   - def guess_a_word(secret_word) ***maybe change it to blank_word***.

5. ask the player to enter *1* character in English each round.
    - def guess_a_letter(): *this should be a while loop*


- 5.1. if the character isn't correct *or* was guessed before
        print *"x"*, and the string of old_letters_guessed. and ask the player to enter another character.
        - def error_check(guess_a_letter): *only* if its not in English
        and over one character *need to fix this*


- 5.2. if the  player enter *only one character is in English*
        check if it is a correct guess or wrong one.
        - def show_hidden_word(secret_word, old_letters_guessed):
         *need to fix this code*

    - 5.2.1  if the guess was correct. show the player the outline of
            the secret_word with the character and blank line.
            - def show_hidden_word(secret_word, old_letters_guessed):
            *old_letters_guessed should be update in 5.2 stage*

    - 5.2.2 if the guess was wrong. print the *"):"* and underneath
            an image of the hangman status according to his number of wrong guesses.
            - def print_hangman(num_of_tries):
            *old_letters_guessed should be update in 5.2 stage*

6. the end of the game: print *"WIN"* if the player gussed the word
      before he ran out of wrong guesses. or print *"LOSE"*
      in case he maxed our his wrong guesses and didnt gussed the word.
      - def check_win(secret_word, old_letters_guessed):
        *need to update this code- maybe compare in to len secret word*

------------------------------------------------------------------------------------
win!!!!!!!!!!!!!!!!
# Print the Welcome Screen

Enter file path: C:\files\words.txt
Enter index: 5

Let’s start!

    x-------x
_ _ _

Guess a letter: ^
X
Guess a letter: T
_ _ t
Guess a letter: b
:(
    x-------x
    |
    |
    |
    |
    |

_ _ t
Guess a letter: c
c _ t
Guess a letter: t
X
b -> c -> t
Guess a letter: p
:(

    x-------x
    |       |
    |       0
    |
    |
    |

c _ t
Guess a letter: a
c a t
WIN
------------------------------------------------------------------------------------
fail!!!!!!!!!!!!!!


# Print the Welcome Screen

Enter file path: C:\files\words.txt
Enter index: 5

Let’s start!

    x-------x
_ _ _

Guess a letter: ^
X
Guess a letter: T
_ _ t
Guess a letter: b
:(
    x-------x
    |
    |
    |
    |
    |

_ _ t
Guess a letter: c
c _ t
Guess a letter: t
X
b -> c -> t
Guess a letter: p
:(

    x-------x
    |       |
    |       0
    |
    |
    |

c _ t
Guess a letter: s
:(

    x-------x
    |       |
    |       0
    |       |
    |
    |

c _ t
Guess a letter: &3
X
b -> c -> p -> s -> t
Guess a letter: M
:(

    x-------x
    |       |
    |       0
    |      /|\
    |
    |

c _ t
Guess a letter: o
:(

    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |

c _ t
Guess a letter: f
:(

    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |

c _ t


-----------------------------------------------------------------------

def hangman_game():
    Welcome_Screen()
    secret_word, char_start = guess_a_word(choose_a_word()) #bring back a tuple
    print("let's play!!")
    # choose_a_word()
    stat_p = 0#to count the num_of_tries
    start_point = print_hangman(stat_p)
    print(start_point)
    print(char_start)#emty char for the secret word
    old_letters = list() #the list that need to be updated

    while check_win(secret_word, old_letters) == False:
        char = guess_a_letter()
        if check_valid_input(char, old_letters) == False:
            break
        elif check_valid_input(char, old_letters) == True:
            if try_update_letter_guessed(char, secret_word, old_letters) == False:
                stat_p = stat_p+1
                show_status = print_hangman(stat_p)
                print(show_status)
            else:
                print(show_hidden_word(secret_word, old_letters_guessed))





                def try_update_letter_guessed(letter_guessed, secret_word, old_letters_guessed):
                    """
                    pass- it need to bring back 3 returns:
                    1.     if letter_guessed not in secret_word:
                            old_letters_guessed.append(letter_guessed)
                            print(":(")
                            foloowed by a hangman_status image
                            and underneath show_correct_letters
                    2. elif letter_guessed in old_letters_guessed:
                        old_letters_guessed = sorted(old_letters_guessed)
                        old_letters_guessed = '->'.join(old_letters_guessed)
                        print("x")
                        print(old_letters_guessed)
                    3. if true
                        show_correct_letters

                    """
                    if letter_guessed not in secret_word:
                        old_letters_guessed.append(letter_guessed)
                        print(":(")
                        # show_correct_letters
                        return "E1"

                    elif letter_guessed in old_letters_guessed:
                        old_letters_guessed = sorted(old_letters_guessed)
                        old_letters_guessed = '->'.join(old_letters_guessed)
                        print("x")
                        print(old_letters_guessed)
                        return "E2"
                    else:  # letter_guessed in secret_word:
                        old_letters_guessed.append(letter_guessed)
                        return True



    def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        """pass"""
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
