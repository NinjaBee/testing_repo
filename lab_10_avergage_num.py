# This lab takes a user created list of numbers and gives back the average of numbers entered. 
import time

numbers = []


while True:
    add_number = input("What number would you like to add to the list? If you do not wish to add any more, type 'done.'").lower()
    if add_number == "done":
        break
    else:
        add_to_list = int(add_number)
        numbers.append(add_to_list)

list_sum = sum(numbers)
list_length = int(len(numbers))

time.sleep(3)
print(f"\nYour list was {str(list_length)} items long.\n")
time.sleep(0.5)
print(f"All the items added together came out to {str(list_sum)}...\n")
time.sleep(2)
print(f"with the average number being {str(list_sum / list_length)}.\n")


