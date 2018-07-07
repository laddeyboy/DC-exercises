bill_total = int(input('Please enter your total bill amount: '))
service_level = input('How was your service? (good, fair, bad)').lower()
tip_amt = 0.00

if service_level == 'good':
    tip_amt = bill_total * .2
    print('Tip amount: $%.2f' %tip_amt)
elif service_level == 'fair':
    tip_amt = bill_total * .15
    print('Tip amount: $%.2f' % tip_amt)
elif service_level == 'bad':
    tip_amt = bill_total * .10
    print('Tip amount: $%.2f' % tip_amt)
    
print('Total of bill + tip is $%.2f' % (bill_total + tip_amt))