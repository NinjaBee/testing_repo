def main():
    while True:
        # Create function with dictionary to convert all acceptable unit measurements. Value is units equivelent to 1 meter. 
        def convert(distance, input_unit, output_unit):
            units = {'meter': 1.0, 'm': 1.0, 'foot': 0.3048, 'feet': 0.3048, 'ft': 0.3048, 'mile': 1609.34, 'mi': 1609.34, 'kilometer': 1000 , 'km': 1000, 'inch': 0.0254, 'in': 0.0254, "yard":0.9144}
        return distance * units[input_unit] / units[output_unit]
        
        # Check if the user wants to convert a unit. If they select n/no exit. 
        run_conversion = input("Would you like to convert one unit of measurment to another? Y/n\n").lower()

        if run_conversion == 'n' or run_conversion == 'no':
            break
        
        # Get the input unit, output unit, and distance

        input_unit = input("What unit would you like to convert from? Valid units are:\n meters, feet, miles, kilometers, yards, and inches.\n")
        distance = float(input(f"How many {input_unit} would you like to convert? Please enter the numerical length only. For example, if you want to convert 10 feet, enter the number 10.\n"))
        output_unit = input(f"What unit would you like to convert {input_unit} to? Valid units are:\n meters, feet, miles, kilometers, yards, and inches.\n")

        #Grab the number we need to show the user by inserting out distance, input and output units into our run_conversion function
        conversion = run_conversion(distance, input_unit, output_unit)

        print(f"{str(distance)} {str(input_unit)} is {str(conversion)} {str(output_unit)}. Wasn't that fun?")

main()