def letter_histogram(word):
    my_dict = {}
    for letter in word:
        if letter in my_dict:
            #the letter is already in the dictionary add 1
            my_dict[letter] = my_dict[letter] + 1
        else:
            #the letter does not exist in the ditionsary
            my_dict[letter] = 1
    return my_dict
    

if __name__ == "__main__":
    new_dict = letter_histogram("supercalifragilisticexpialidocious")
    print(new_dict)