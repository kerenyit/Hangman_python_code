#write a message for the player and ask for a word
guess_a_word=input("Please enter a word:" )

#compute the length of the word
length_of_the_guessed_word = len(guess_a_word)
string_of_char_word = "_ " * length_of_the_guessed_word

#print an image of empty position based on the length of the word
print(string_of_char_word)
