a_num = int(input('Enter a number: '))

for x in range(a_num, 0, -1):
    if(a_num % x == 0):
        print(x)