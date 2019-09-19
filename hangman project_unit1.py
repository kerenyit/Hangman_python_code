#hangman project - first unit.
# wtite  the name of the game and draw the images for the wrong gusses.
# limit your gusses by using randint function


#the name of the game:
HANGMAN_ASCII_ART = print(""" _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/  |
                   |____ / """)

# limit gusses by using randint function
MAX_TRIES= random.randint(5,10)
print(MAX_TRIES)

guess_a_letter= input("Guess a letter:" )
guess_a_letter.lower()
print(guess_a_letter)

#images for the wrong gusses

#picture 1:
print("x-------x")
#picture 2:
print("""x-------x
|
|
|
|
|""")
#picture 3:
print("""x-------x
|       |
|       0
|
|
|""")
#picture 4:
print("""x-------x
|       |
|       0
|       |
|
|""")
#picture 5:
print("""x-------x
|       |
|       0
|      /|\\
|
|""")
#picture 6:
print("""x-------x
|       |
|       0
|      /|\\
|      /
|""")
#picture 7:
print("""x-------x
|       |
|       0
|      /|\\
|      / \\
|""")
