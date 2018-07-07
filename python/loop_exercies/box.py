width = int(input('Enter Width: '))
height = int(input('Enter Height: '))


print('*' * width)
for x in range(height-2):
    print('*' + ' ' * (width-2) + '*')
print('*' * width)