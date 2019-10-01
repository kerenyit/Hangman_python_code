# write a message for the player and ask for a word
#guess_a_word=input("Please enter a word:" )


def empty_char(secret_word):

    # compute the length of the word
    length_secret_word = len(secret_word)
    temp_string_secret_word = "_ " * length_secret_word

# print an image of empty position based on the length of the word
    print(temp_string_secret_word)
