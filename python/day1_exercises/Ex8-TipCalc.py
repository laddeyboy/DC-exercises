bill_total = int(input('Please enter your total bill amount: '))
service_level = input('How was your service? (good, fair, bad)').lower()
num_ppl = int(input('How many people we\'re at dinner? '))
tip_amt = 0.00

if service_level == 'good':
    tip_amt = bill_total * .2
elif service_level == 'fair':
    tip_amt = bill_total * .15
elif service_level == 'bad':
    tip_amt = bill_total * .10

print('Tip ammount: ${:.2f}'.format(tip_amt))    
print('Total bill amount ${:.2f}'.format(bill_total + tip_amt))
print('Amount per person ${:.2f}'.format((bill_total + tip_amt)/num_ppl))