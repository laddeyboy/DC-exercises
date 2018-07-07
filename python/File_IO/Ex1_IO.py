file_name = input('Enter a file name: ')

#future state would be to verfiy the file input string for validity

file_handle = open(file_name, 'r')
file_contents = file_handle.read()
file_handle.close()

print(file_contents)