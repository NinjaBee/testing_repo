# This lab is to create a simple REPL (read evaluate print loop) calculator
# capable of subtraction, addition, division, and multiplication. 
# It will be broken into two options... entering each number and operand seperately, 
# and using the eval function to evaluate a full equation. 

def main(): 
    print("Welcome.")
    while True:
        select_calc = input("Would you like to evaluate a full equation, enter individual numbers, or exit the program?\n\
            \n Please enter one of the following numbers... \n 1: Evaluate a full equation. \n 2: Enter equation manually. \n 3: Exit.\n")
        
        if select_calc == "3":
            break 
        elif select_calc == "1":
            pass 
        elif select_calc == "2":
            def minus(num1, num2):
                return num1 - num2
            def add(num1, num2):
                return num1 + num2
            def multiply(num1, num2):
                return num1 * num2
            def divide (num1, num2):
                return num1 / num2

            operation = input("What operation would you like to use? You may choose from - + / or * \n")
            first_num = float(input("\nWhat is the first number?\n"))
            second_num = float(input("\nWhat is the second number\n?"))

            operation_dict = {
                "-": minus, "+": add, "/": divide, "*": multiply
                }

            answer = operation_dict[operation](first_num,second_num)

            print(f"\nCongratulations! You have {str(answer)} elephants!")

            print(answer)
            
        else:
            print("Please try again.")

main()