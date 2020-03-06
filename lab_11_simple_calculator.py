# This lab is to create a simple REPL (read evaluate print loop) calculator
# capable of subtraction, addition, division, and multiplication. 
# It will be broken into two options... entering each number and operand seperately, 
# and using the eval function to evaluate a full equation. 
import time 

def main(): 
    print("Welcome.")
    while True:
        select_calc = input("Would you like to evaluate a full equation, enter individual numbers, or exit the program?\n\
            \n Please enter one of the following numbers... \n 1: Evaluate a full equation. \n 2: Enter equation manually. \n 3: Exit.\n").lower()
        
        if select_calc == "3" or select_calc == "exit":
            break 
        elif select_calc == "1":
            calculation = input("Please type in your math problem: \n >")
            time.sleep(1)
            print(f"\nCongratulations! You have {str(eval(calculation))} fruit bats!\n")
        elif select_calc == "2":
            #Create functions to do the maths
            def minus(num1, num2):
                return num1 - num2
            def add(num1, num2):
                return num1 + num2
            def multiply(num1, num2):
                return num1 * num2
            def divide (num1, num2):
                return num1 / num2
            
            # Create dictionary to hold functions values associated with symbols. 
            operation_dict = {
                "-": minus, "+": add, "/": divide, "*": multiply
                }

            # Gather the operand and numbers to be calculated.
            operation = input("What operation would you like to use? You may choose from - + / or * \n")
            first_num = float(input("\nWhat is the first number?\n"))
            second_num = float(input("\nWhat is the second number?\n"))

            # Do some math
            answer = operation_dict[operation](first_num,second_num)

            time.sleep(1)

            # Let the user see their answer. 
            print(f"\nCongratulations! You have {str(answer)} elephants!")
            
        else:
            print("Please try again.")

main()