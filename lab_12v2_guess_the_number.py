import random 

computer_guess = random.ranint(1,1000)

guess_count = 0
guess_history = []

def main():
    while True:
        user_guess = input("Guess a number between 1 and 1000.")
        try:
            user_num = int(user_guess)
            if user_num == computer_guess:
                print(f'Congratulations! It was {str(computer_guess)}! It took you {str(guess_count + 1)} to get it!')
                break
            elif user_num > computer_guess:
                if not guess_history:
                    print(f"Sorry! {str(user_num)} is too high!")
                    guess_history.append(user_num)
                else:
                    if (computer_guess - user_num) < (computer_guess - guess_history[-1]):
                        print("Whoops! You're getting colder! Still too high.")
                        guess_history.append(user_num)
                    elif (computer_guess - user_num) > (computer_guess - guess_history[-1]):
                        print("Alright! You're getting warmer. Still too high, though.")
                        guess_history.append(user_num)
