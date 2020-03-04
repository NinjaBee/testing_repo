import random 
import time

magic_answers = ['It doesn\'t look good...', 'Don\'t look behing you.', 'Yes.', 'No.', \
    'There is a great chance!', 'Just do your best.']

def main():
    
    running = True 

    while running == True: 
        get_answer = input('Ready to have your future told? \n \
            \n If you would like to ask the 8 ball a question, type "ask"\n \
            \n If you would like to think and come agian another day type "q."\n:').lower()
        
        if get_answer == 'ask':
            question = input('Meditate on your question. Do you have it? When you are ready type "y" and hit enter....\n:')
            time.sleep(1)
            print(random.choice(magic_answers).upper())
            time.sleep(2)

        elif get_answer != 'ask':
            print("Yeah...I wouldn't want to know the answer either.\n \n ")
            break

main()

