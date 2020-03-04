import random 
import time

magic_answers = ["It doesn't look good...", "Don't look behing you.", "Yes.", "No.", \
    "There is a great chance!', 'Just do your best.", "It's highly likely!", "Odds are good!",\
     "Stranger things have happened...", "I wouldn't count on it.", "Good things happen to good people.", \
         "You get what you deserve.", "Just ask yourself....what would Scooby do?",]

def main():
    
    running = True 

    while running == True: 
        # The "\x1b[1;37;40m" bit is for adjusting how the text displays in the terminal.
        get_answer = input("\x1b[1;37;40m" + 'Ready to have your future told? \n \
            \n If you would like to ask the 8 ball a question, type "ask"\n \
            \n If you would like to think and come agian another day type "q."\n:').lower()
        
        if get_answer == 'ask':
            question = input('Meditate on your question. Do you have it? When you are ready type "y" and hit enter....\n:')
            # time.sleep is being used in this block to add rhythm for the user.
            time.sleep(1)
            #Text color is being altered for the answer. I also decided to make answers upper case here. 
            print("\n \x1b[1;35;40m" +random.choice(magic_answers).upper() + "\x1b[1;37m \n" )
            time.sleep(2)

        elif get_answer != 'ask':
            print("Yeah...\n")
            time.sleep(2)
            print("I wouldn't want to know the answer either...\n \n ")
            time.sleep(1)
            break

main()

