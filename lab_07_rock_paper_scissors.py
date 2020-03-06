

# If you convert rock paper and scissors into numbers (1, 2, 3) \
# and subtract one number from the other there are patterns... 0 is always a tie. \ 
# Should be able to build more condensed version of game with this instead of simply \
# going through all outcomes individually. 

# If rock = 1, paper = 2, and scissors = 3 ... -2 = Win | -1 = lose | 0 = tie | 1 = Win | 2 = Lose

# rock (1) - rock (1) = 0         -> tie 
# rock (1) - paper (2) = -1       -> Lose (paper covers rock)
# rock (1) - scissors (3) = -2    -> Win (Rock smashes scissors)

# paper (2) - rock (1) = 1        -> Win (paper covers rock)
# paper (2) - paper (2) = 0       -> tie 
# paper (2) - scissors (3) = -1   -> Lose  (scissors cuts paper) 

# scissors (3) - rock (1) = 2     -> Lose (rock smashes scissors)
# scissors (3) - paper (2) = 1    -> Win (scissors cuts paper)
# scissors (3) - scissors (3) = 0 -> tie 

# Wins are -2, and 1 
# Loses are -1, and 2 
# tie is 0 
# Any other number is not valid. 

#So... if I build a dictionary with the values tied to rock, paper and scissors and the \
# user accesses that dictionary... I should be able to use the value to determine who wins. 

import time
import random 


game_dict = {"rock": 1, "paper": 2, "scissors": 3}

def main():
    while True:

        game_prompt = input("If you would like to play type in 'rock,' 'paper,' or 'scissors.' Otherwise type in 'q' to quit.\n").lower()
        

        if game_prompt == 'q' or game_prompt == 'quit':
            time.sleep(1)
            print("See you later.")
            break
        elif game_prompt == 'rock' or game_prompt == 'paper' or game_prompt == 'scissors':

            possible_answers = [1,2,3]
            computer_answer = random.choice(possible_answers) 
            human_answer = game_dict[game_prompt]

            if human_answer - computer_answer == -2 or human_answer - computer_answer == 1:
                print("You win!")
                time.sleep(1)
            elif human_answer - computer_answer == -1 or human_answer - computer_answer == 2:
                print("You lose! Sorry!\n")
                time.sleep(1)
            else:
                print("It's a tie!\n")
                time.sleep(1)
        else:
            print("Please try again. I did not understand.\n ")

main()