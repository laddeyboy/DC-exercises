my_phonebook = {
    'Josh': {'phone':'555-555-5555', 'email': 'joshua@yahoo.com', 'website': 'www.linkedin.com/josh'},
    'Amy': {'phone':'444-444-4444', 'email': 'amy@yahoo.com', 'website': 'www.linkedin.com/amy'},
    'Tina': {'phone':'333-333-3333', 'email': 'tina@yahoo.com', 'website': 'www.linkedin.com/tina'}
    }

def print_menu(): 
    print('E-Phone Book') 
    print('_______________________') 
    print('1. Search Contacts') 
    print('2. Create Contact') 
    print('3. Delete Contact') 
    print('4. Display all Contacts') 
    print('5. Quit Phone Book') 

def search_contacts():
    pass

def add_contact():
    new_contact = {}
    print('----------Adding new contact----------')
    temp = input('Enter contact name: ')
    new_contact['phone'] = input('Enter contact phone: ')
    new_contact['email'] = input('Enter contact email: ')
    new_contact['website'] = input('Enter contact website: ')
    print('--------------------------------------')
    my_phonebook[temp] = new_contact

def print_phonebook():
    for key in my_phonebook.keys():
        print('{} -->>'.format(key))
        print('Phone: {}'.format(my_phonebook[key]['phone']))
        print('Email: {}'.format(my_phonebook[key]['email']))
        print('Website: {}'.format(my_phonebook[key]['website']))
        print('\n')
    

def main(): 

    while(True): 
        print_menu() 
        choice = int(input('What do you want to do: ')) 
        if(choice == 1): 
            search_contacts()
        elif(choice == 2): 
            #do something 
            add_contact()
        elif(choice == 3): 
            #do something
            pass
        elif(choice == 4): 
            #do something 
            print_phonebook()
        elif(choice == 5): 
            print('Exiting...') 
            break 
        else: 
            print('You entered an invalid selection.  Try Again!')
            
            
if __name__ == '__main__':
    main()