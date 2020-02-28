from random import choice 
#chooses a random item from a list and removes that item from the list. 
def choose(a_list):
    rand_item = choice(a_list)
    a_list.remove(rand_item)
    return rand_item

def main(): 
    user_input = []
    # Create seperate lists... and seperate prompts? 

    prompts = [
        '\n Give me an antonym for \'data\' : ',
        'Give me a noun: ',
        'Give me an adjective: ',
        'A type of animal', #8 of these
    ]

    while True:
        for prompt in prompts:
           user_input.append(input(prompt))

        #This is where additional "for noun in nouns:" etc prompt type for loops would go.
        # Name your {choose(xyz)} bit correctly to go with nouns or verbs, etc. 
        madlib = f"\n{choose(user_input)} scientist Job Description:\
            \nSeeking a {choose(user_input)} engineer, able to work on {choose(user_input)} projects with a team of {}. \
            \nKey responsibilities:\
            \n - Extract patterns from {choose(user_input)}\
            \n - Optimize {choose(user_input)}choose(user_input)\
            \n - Transform {choose(user_input)} into {user_input[0]} material."

    print(madlib)

    if(input('\nWould you like to make another? (y/n):').lower() != 'y'):
        print("I don't blame you. I don't like madlibs either.\n")
        break
main()