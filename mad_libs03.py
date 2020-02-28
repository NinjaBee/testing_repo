import random # from random import choice. With just "import random" must type random.choice to use. 
#with from random import choice you can say "choice(a_list)" but may have nameing


continue_game = input("Would you like to play madlibs? yes or no?\n:")

while continue_game == "yes":
    adj_1 = input("Hello. We are going to do another mad lib. Give me an adjective!\n:")
    adj_2 = input("I need another adjective\n:")
    adj_3 = input("Okay, one more:\n:")
    obj_1 = input("Now give me an object.\n:")
    obj_2 = input("Another object.\n:")
    obj_3 = input("Final object. :-)\n:")

    adj_list = [adj_1, adj_2, adj_3]
    obj_list = [obj_1, obj_2, obj_3]

    print("Oh my! What a " + random.choice(adj_list) + " piece of " + random.choice(obj_list) + "!  I don't know how you got that " + random.choice(obj_list) + ", but it is very " + random.choice(adj_list) + "!")
    continue_game = input("Would you like to play again?\n:")
else:
    print("Goodbye!")