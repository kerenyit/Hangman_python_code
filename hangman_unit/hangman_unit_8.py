def print_hangman(num_of_tries):
    """
    VARIABLE-  HANGMAN_PHOTOS (dict)- from unit 1
    the FUNCTION PRINT:
    one of the 7 photos in HANGMAN_PHOTOS-
    with the help of a VARIABLE-num_of_tries that represent
    how many times the user
    guessed the wrong letter, and  HANGMAN_PHOTOS
    dict[key] = value
    """
    # images for the wrong gusses

    # picture 1:
    image1 = "x-------x"
    # picture 2:
    image2 = """x-------x
|
|
|
|
|"""
    # picture 3:
    image3 = """x-------x
|       |
|       0
|
|
|"""
    # picture 4:
    image4 = """x-------x
|       |
|       0
|       |
|
|"""
    # picture 5:
    image5 = """x-------x
|       |
|       0
|      /|\\
|
|"""
    # picture 6:
    image6 = """x-------x
|       |
|       0
|      /|\\
|      /
|"""
    # picture 7:
    image7 = """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""

    HANGMAN_PHOTOS = {0: image1, 1: image2, 2: image3, 3: image4, 4: image5, 5: image6, 6: image7}

    if num_of_tries in HANGMAN_PHOTOS.values():
        # if value in HANGMAN_PHOTOS.values():
        print("x")
        print(num_of_tries)
    # print(HANGMAN_PHOTOS[num_of_tries])


num_of_tries = 6
print_hangman(num_of_tries)
num_of_tries = 0
print_hangman(num_of_tries)
num_of_tries = 3
print_hangman(num_of_tries)
