
def choose_a_word(file_path, index):
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
    fhand.close()
    i_count = index-1
    if index > count:
        i_count = (i_count) % len(text_l)
        # print(i_count)
    chosen_word = count, w[i_count]
    return chosen_word


secret_word = choose_a_word(input("enter a file name:"), int(input("enter a number:")))
print(secret_word)
