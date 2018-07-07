class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_friends = []

    def greet(self, other_person):
        self.greeting_count += 1
        self._am_I_unique(other_person)
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
    
    def print_contact_info(self):
        print("{name}'s email: {email}, {name}'s phone number: {number}".format(name=self.name, email=self.email, number=self.phone))
    
    def add_friend(self, a_Person):
        self.friends.append(a_Person)
    
    def num_friends(self):
        return len(self.friends)
        
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
        
    def _am_I_unique(self, a_Person):
        if a_Person not in self.unique_friends:
            self.unique_friends.append(a_Person)
        
    def num_unique_people_greeted(self):
        return len(self.unique_friends)
        
        
#1
sonny = Person('Sonny', 'sony@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# sonny.greet(jordan)
# jordan.greet(sonny)
print('I am {} my email is {} and my number is {}'.format(sonny.name, sonny.email, sonny.phone))
print('I am {} my email is {} and my number is {}'.format(jordan.name, jordan.email, jordan.phone))
print('-------Extra Person Methods----------')
sonny.print_contact_info()
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# print("I have this many friends {}".format(len(jordan.friends)))
jordan.add_friend(sonny)
sonny.add_friend(jordan)
print('I have {} friends.'.format(sonny.num_friends()))

sonny.greet(jordan)
sonny.greet(jordan)
deeAnn = Person('Sonny', 'sony@hotmail.com', '483-485-4948')
Roger = Person('Sonny', 'sony@hotmail.com', '483-485-4948')
sonny.greet(deeAnn)
sonny.greet(Roger)

print("Unique Friends: {}".format(sonny.num_unique_people_greeted()))



class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def print_info(self):
        print('{} {} {}'.format(self.year, self.make, self.model))
        
#2
print('-------Vehicle Methods----------')
car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()