my_string = "Josh Ladwig"

#Uppercase
print(my_string.upper())

#Capitalize String
print(my_string.capitalize())

#Reverse String
print(my_string[::-1])

#Leetspeak
#tranlator = [(A,4), (E,3), (G,6), (I,1), (O,0), (S,5), (T,7)]
a_word = "LEET"
print("I'm starting with: {}".format(a_word))
a_word = a_word.upper()
a_word = a_word.replace('A','4')
a_word = a_word.replace('E','3')
a_word = a_word.replace('G','6')
a_word = a_word.replace('I','1')
a_word = a_word.replace('O','0')
a_word = a_word.replace('S','5')
a_word = a_word.replace('T','7')
print("My leet word is: {}".format(a_word))


#Long-long Vowels
word = "cheese"
long_vowel = "cheese"
long_vowel = long_vowel.replace('ee', 'eeeee')
long_vowel = long_vowel.replace('oo', 'ooooo')
print("{} => {}".format(word, long_vowel))

#Caesar Cipher
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'nopqrstuvwxyzabcdefghijklm'
my_code = "lbh zhfg hayrnea jung lbh unir yrnearq"
final = []

for letter in my_code:
    if(letter == ' '):
        final.append(' ')
    else:
        index = alphabet.find(letter)
        final.append(cipher[index])
    
print(''.join(final))

