import random 
import string 
import time

#string.ascii_letters 
#string.ascii_lowercase 
#string.ascii_uppercase 
#string.digits 
#string.punctuation

# ask user for how many lower case letters, how many uppercase letters, numbers, and 
# special characters they want in their string. Generate password accordingly.

password_characters = [random.choice(string.ascii_letters), \
         random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase),\
         random.choice(string.digits), random.choice(string.punctuation),]

password_string = ""

create_password = input("Would you like to create a password? Y/n \n:").lower()

if create_password == "y" or create_password == "yes":
    specify_password = input("Would you like to specify how many uppercase, lowercase, numbers, \
        and special characters there are in your password? Y/n \n:").lower()

    if specify_password == "y" or specify_password == "yes":
        random_characters = []

        num_uppercase_letters = input("How many uppercase letters would you like?")
        num_lowercase_letters = input("How many lowercase letters would you like?")
        num_digits = input("How many digits would you like?")
        num_punctuation = input("How many special characters would you like?")

        def add_together(upper, lower, digits, punctuation):
            upper_num = int(upper)
            lower_num = int(lower)
            digits_num = int(digits)
            punctuation_num = int(punctuation)
            
            total_length = upper_num + lower_num + digits_num + punctuation_num
            
            return total_length

        for uppercase in range (0, num_uppercase_letters):
             random_characters.append(password_characters[2])

        for lowercase in range (0, num_lowercase_letters):
            random_characters.append(password_characters[1])
        
        for digits in range (0, num_digits): 
            random_characters.append(password_characters[3])
        
        for punctuation in range (0, num_punctuation):
            random_characters.append(password_characters[4])
        
        total_length = add_together(num_uppercase_letters, num_lowercase_letters, num_digits, num_punctuation)

        for password in range (0, total_length):
            password_string = password_string + random.choice(random_characters)

        print(password_string)
        
    elif specify_password == "n" or specify_password == "no"
        password_length = int(input("How long would you like your password to be? \n \
     Please enter a number.\n:"))
        for password in range (0, password_length):
            password_string = password_string + random.choice(password_characters)
        print(password_string)
elif create_password == "n" or create_password == "no": 
    print("Ok! Just don't use the same password twice... ")
    time.sleep(2)
    break 
else:
    print("....um... ok.... ")
    time.sleep(1)
    break