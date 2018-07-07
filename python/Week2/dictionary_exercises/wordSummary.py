def word_histogram(paragraph):
    text = paragraph.lower().split()
    my_dict = {}
    for words in text:
        if words in my_dict:
            #the word is already in the dictionary add 1
            my_dict[words] = my_dict[words] + 1
        else:
            #the word does not exist in the ditionsary
            my_dict[words] = 1
    return my_dict
    

if __name__ == "__main__":
    new_dict = word_histogram("To be or not to be")
    print(new_dict)