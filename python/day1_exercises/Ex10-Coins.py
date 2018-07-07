count = 0
while True:
    print('You have {} coins'.format(count))
    choice = input('Do you want a coin? ')
    if choice == "yes":
        count += 1
    elif choice == "no":
        print('Bye')
        break
        