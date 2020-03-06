# This lab takes a user created list of numbers and gives back the average of numbers entered. 

numbers = []

keep_adding == True 

while keep_adding == True:
    add_number = input("What number would you like to add to the list? If you do not wish to add any more, type 'done.').lower()
    if add_number == "done":
        keep_adding = False 
    else:
        keep_adding = True 
    add_number = int(add_number)
    numbers.append(add_number)

list_sum = sum(numbers)
list_length = int(len(numbers))

print(f"Your list was {str(list_length)} items long. All the items added together came out to {str(list_sum)} with the average number being {str(list_sum / list_length)}.")

