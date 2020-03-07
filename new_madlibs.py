import random

def select_word(some_list):
    word = random.choice(some_list)
    some_list.remove(word)
    return word

def main():

    while True:
        city_name = input('Name a city you know ...or one from Harry Potter.')
        direction = input('State a direction... eg. Left, South...')

        nouns_prompt = input('Please list 13 random nouns\n')
        plural_n_prompt = input('Please list three plural nouns\n')
        verbs_prompt = input('Please list three verbs. ex: "run"\n')
        past_v_prompt = input('Please list three past tense verbs.\n')
        ing_v_prompt = input('Please list five verbs ending in -ing.\n')
        adj_prompt = input('Please list six adjectives.\n')
        body_part_prompt = input('Please list three body parts.\n')

        nouns = nouns_prompt.split()
        plural_nouns = plural_n_prompt.split()
        verbs = verbs_prompt.split()
        past_verbs = past_v_prompt.split()
        ing_verbs = ing_v_prompt.split()
        adjectives = adj_prompt.split()
        body_parts = body_part_prompt.split()

        print(adjectives)
        print(nouns)
        print(plural_nouns)

        


        print(f'Harry Potter MadLib #1\
         \(by Elanor Gamgee \) Taken from Chapter Five, \
         "The Whomping Willow" in Harry Potter and the Chamber \
        of Secrets" Check that no one\'s {select_word(ing_verbs)}," said Ron, \
        starting the {select_word(nouns)} with another tap of his\
        {select_word(nouns)}. Harry stuck his {select_word(body_parts)} out \
        of the {select_word(nouns)}: {select_word(nouns)} was fumbling \
        along the main {select_word(nouns)} ahead, but their street\
        was {select_word(adjectives)} . "Okay," he said.\
        Ron pressed a {select_word(adjectives)} silver {select_word(nouns)} \
        on the {select_word(nouns)} . The {select_word(nouns)} around\
        them {select_word(past_verbs)} -- and so did they.\
        Harry could feel the {select_word(nouns)} {select_word(ing_verbs)} \
        beneath him, {select_word(verbs)} the {select_word(nouns)}, \
        feel his {select_word(body_parts)} on his knees and his {select_word(nouns)} on his nose, but for all he could {select_word(verbs)} , \
        he had become a pair of {select_word(plural_nouns)}, {select_word(ing_verbs)} a few feet above the ground in a dingy street full of\
        parked cars. "Let\'s go," said Ron\'s voice from his {direction}. And the {select_word(nouns)} and the {select_word(adjectives)} \
        {select_word(plural_nouns)} on either side {select_word(past_verbs)} away, {select_word(ing_verbs)} out of site as the {select_word(nouns)} \
        rose; in seconds, the whole of {city_name} lay, {select_word(adjectives)} and {select_word(adjectives)} below them.')

       # print(madlib)

        keep_going = input("Would you like to play again? Y/n\n").lower()

        if keep_going == "y" or keep_going == "yes":
            print("ok... if you're sure. It will be the same madlib...")
        else:
            break

main()








# def insert_noun():
#     for noun in nouns
#         this_noun = nouns[x]  #could make this a random choice and pop off... ?
#     x += 1
#     return this_noun





# How many nouns: 12
# How many plural nouns: 2
# How many verbs: 2
# Verb past tense: 2
# Verb - ing: 3
# How many Adjectives: 5 
# How many body parts: 2 
# City Name: 1
# Direction: 1 

# needed_words = ["nouns", "plural nouns", "verbs", "verb, past tense", "-ing verb", "body part", "body parts", "adjective", "city name", "direction"]
# Do I want to make seperate lists to draw from, or replace the words as I come accross them and prompt the user along the way? 
 