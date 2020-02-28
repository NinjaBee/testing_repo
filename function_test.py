# This is not the way to insert into the madlib. 

nouns = ["coffee", "tea", "milk"]

#new_noun = nouns.append(input("Please type a noun.\n:")

#Defining x
x = 0 # No  real meaning unless it is being incremented in a loop or altered outside the function. 

# This only grabs a noun at nouns[x]
def insert_noun(x):
    this_noun = nouns[x]
    x += 1
    # print(this_noun) ? Should I print instead? My f-string doesn't like my quotes and my
    #definition of x outside of the function is not being registered either. Why? - Not in loop.
    # print(this_noun)
    print(x)
    return this_noun

# Defining what to do when a_noun is called in f-string. 


# output = f'This kid likes {insert_noun()} and {insert_noun()}. What do you like... {insert_noun()}?'
# print(f"This kid likes {insert_noun()} and {insert_noun()}. What do you like... {insert_noun()}?")

print(f"OUTPUT HERE {insert_noun(x)}") 

# print(output)