import random 

computer_choice = random.randint(1,10)

guess_count = 0 

while guess_count <= 10:
    while True:
        user_guess = input("Guess a number between 1 and 10.  For example '6.'\n:")
        try: 
            guess_num = int(user_guess)
            #return guess_num
            break
        except TypeError:
            print("Oops! Please only enter numerals. :-) ")

    if guess_num == computer_choice:
        print(f"You're right! The computer selected {str(computer_choice)}. You guessed {str(guess_count)} times!")
        break
    elif guess_num > computer_choice:
        print("Oops! That was a little too high!")
    elif guess_num < computer_choice:
        print("Sorry! That one was too low...")

    guess_count += 1 

    

