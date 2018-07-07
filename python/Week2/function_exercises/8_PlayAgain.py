def playagain():
    user_input = input("Do you want to play again (Y or N)? ")
    if(user_input == 'Y'):
        return True
    else:
        return False
        
if __name__ == "__main__":
    playagain()