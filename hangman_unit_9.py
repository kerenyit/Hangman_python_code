
"""
the FUNCTION will choose a word from a 'file.txt' that contains words seprated
by spaces
PARAM:
file_path= STRING that represent the path to the file
index= intnger that represent the place of a specific word in the file

the FUNCTION returns:
TUPLE- with two parmaters it the order-
1. counts=the number of words in the file. without repeating words.
2. index= a word that was return as an argument for the index FUNCTION- thisword
will use as the secret secret_word.

instructions:
begin index count from 1 and not 0.
if index is bigger than the number of words in he file, the FUNCTION
continue to count from the beginning

example for the file.txt:

hangman song most broadly is a song hangman
work music work broadly is typically """


def choose_word(file_path, index):
    fhand = open(file_path, 'r')
    count = 0
    text_l = list()
    w = list()
    for line in fhand:
        words = line.split()
        for word in words:
            text_l.append(word)
            if word not in w:
                count += 1
                w.append(word)
    i_count = index-1
    if index > count:
        i_count = (i_count) % len(text_l)
        # print(i_count)
    chosen_word = count, w[i_count]
    return chosen_word

# file_path.close()


file_path = r"C:\users\orkat\git\or12k\wind10demo\w.txt"  # input('Enter the file name: ')
index = 3

print(choose_word(file_path, index))

#
