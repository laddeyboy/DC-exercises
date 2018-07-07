from wordSummary import *
from letterSummary import *

file_name = input('Enter a file name: ')

#future state would be to verfiy the file input string for validity

file_handle = open(file_name, 'r')
file_contents = file_handle.read()
file_handle.close()

print("Word Histogram:")
print(word_histogram(file_contents))

print("Letter Histogram")
print(letter_histogram(file_contents))