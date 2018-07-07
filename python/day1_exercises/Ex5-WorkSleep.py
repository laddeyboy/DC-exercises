day = int(input('Day (0-6)? '))

if day == 0 or day == 6: print('Sleep in')
elif day > 0 and day < 6: print('Go to work')
else: print('Not a valid date')