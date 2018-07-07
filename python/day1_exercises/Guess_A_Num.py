import random
secret_num = random.randint(1,10)
guesses_left = 5
keep_playing = True

while keep_playing:
    print("I am thinking of a number between 1 and 10...")
    while guesses_left > 0:
        print("You have {} guess left.".format(guesses_left))
        guess = int(input("Guess a number? "))
        guesses_left -= 1
        if guess == secret_num:
            print("Yes! You Win!")
            break
        else:
            if(guess > secret_num):
                print(guess, "is too high.")
            elif(guess < secret_num):
                print(guess, "is too low.")
                
    print("You ran out of guesses!")
    play_time = input("Do you want to play again? (Y/N)").lower()
    if play_time == 'n':
        keep_playing = False
    elif play_time == 'y':
        guesses_left = 5
        secret_num = random.randint(1,10)
    else:
        print("You entered an invalid input....playing again!")
        guesses_left = 5
        secret_num = random.randint(1,10)
        