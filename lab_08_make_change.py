def main():
    def dollars_to_pennies():
        amount = float(input("Please enter a dollar amount. For example for $1.20, you would enter 1.20 \nThank you! \n Amount:"))
        pennies = int(amount *100)
    

        print("You have " + str(pennies) + " pennies.")
        
    def pennies_to_dollars():
        amount = int(input("Please enter the number of pennies you want to convert. \n Amount:"))
        dollars = amount // 100
        pennies = amount % 100
        
        print("You have " + str(dollars) + " dollars and " + str(pennies) + " cents." )


    print("Welcome to the change converter. I promise not to eat your money... hmm... but first...")

    dollars_or_pennies = input("Would you like to either a: Convert pennies to dollars. \n or b: Convert dollars to pennies? \n Please select either a or b.").lower()

    if dollars_or_pennies == "a":
        pennies_to_dollars()
    elif dollars_or_pennies == "b":
        dollars_to_pennies()
    else:
        print("Sorry. I didn't catch that.")

main()