file_name = input('Enter a file name: ')

file_handle = open(file_name, 'w')
file_contents_to_write = input('What to add: ')
file_handle.write(file_contents_to_write)
file_handle.close()