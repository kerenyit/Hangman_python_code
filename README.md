## **Hangman- python**

This is a simple Hangman game written in python. This project was made as the final assignment in a self.py course.

## **Requirments**
Python 3.

## **Pseudo code**
This is the pseudo code I created for the game:

1. first print a Welcome_Screen
    - def Welcome_Screen():with the name of the game and number of possible wrong answers.

2. ask the player to enter a file and a number:
    - def choose_a_word(): this will return the secret_word he will
    had to guess.

3. show the player his current status of the game.
    - def print_hangman(num_of_tries): according to his number of wrong guesses- in the beginning its the first one.

4. underneath the image of the hangman. show the status of the secret_word
   in blank lines.
   - def guess_a_word(secret_word) 

5. ask the player to enter *1* character in English each round.
    - def guess_a_letter(): *this should be a while loop*


- 5.1. if the character isn't correct *or* was guessed before
        print *"x"*, and the string of old_letters_guessed. and ask the player to enter another character.
        - def error_check(guess_a_letter): *only* if its not in English
        and over one character 


- 5.2. if the  player enter a charcer (only one character is in English)
        check if it is a correct guess or wrong one.
        - def show_hidden_word(secret_word, old_letters_guessed):
         

    - 5.2.1  if the guess was correct. show the player the outline of
            the secret_word with the character and blank line.
            - def show_hidden_word(secret_word, old_letters_guessed):
            

    - 5.2.2 if the guess was wrong. print the *"):"* and underneath
            an image of the hangman status according to his number of wrong guesses.
            - def print_hangman(num_of_tries):
            *old_letters_guessed should be update in 5.2 stage*

6. the end of the game: print *"WIN"* if the player gussed the word
      before he ran out of wrong guesses. or print *"LOSE"*
      in case he maxed our his wrong guesses and didnt gussed the word.
      - def check_win(secret_word, old_letters_guessed):
       

