# 1. Basic Calculator & Temperature Converter
# Skills practiced:

# Reading user input with input()

# Converting between str and numeric types (int, float)

# if/elif/else branching

# Defining and calling simple functions

# Description:

# Prompt the user for two numbers and an operation (+, -, *, /), then print the result.

# Add a second mode: convert Celsius ↔ Fahrenheit. Ask the user which mode (calculator vs. converter).

# Loop until the user types “exit.”

# Suggested extensions:

# Handle division by zero with a try/except.

# Allow the user to chain calculations (e.g. “continue with the previous result”).

# Keep a history list of past calculations and let the user review it.

while True:
    mode = None
    while mode not in (1,2):
        try: 
            mode = int(input("1: calculator \n2: temperature converter \n:"))
        
            if mode not in(1,2):
                print("\nThat isn't one of the options\n")
        
        except ValueError:
            print("\nThat isnt one of the options\n")

    #calculator
    if mode == 1:
        print("\nThis is the calculator")

        op1 = None

        #loop to prevent wrong input of operator
        while op1 not in("+","-","*","/"):
            op1 = input("\nWhat operation do you want to use? (+,-,*,/)\n:")

            if op1 not in ("+","-","*","/"):
                print("\nThat isnt one of the operations")


        num1 = None

        #loopa to prevent wrong input of number
        while num1 == None:
            try:
                num1 = float(input("\nWhat is the first number\n:"))

            except ValueError:
                print("\nThats not a number")

        num2 = None
        while num2 == None:
            try:   
                num2 = float(input("\nWhat is the second number\n:"))
                #handle divide by zero exception
                if op1 == "/" and num2 == 0:
                    print("\nError: dividing by zero\n")
                    num2 = None

            except ValueError:
                print("\nThats not a number")


        if op1 == "+":
            val = num1 + num2
        elif op1 == "-":
            val = num1 - num2
        elif op1 == "*":
            val = num1 * num2
        elif op1 == "/":
            val = num1 / num2
        else:
            print("\nsomething went wrong in choosing the operator")

        print(num1, op1, num2, "=", val)

        result_str = f"{num1} {op1} {num2} = {val}"



        past_calc = []
        past_calc.append(result_str)
        #adding option to chain operations

        while True:

            cont = input("\nWould you like to apply more operations onto the result? (y/n)").strip()

            if cont not in ("y", "yes"):
                break
            op = None

            #loop to prevent wrong input of operator
            while op not in("+","-","*","/"):
                op = input("\nWhat operation do you want to use? (+,-,*,/)\n:").strip()

                if op not in ("+","-","*","/"):
                    print("\nThat isnt one of the operations")


            num = None
            while num == None:
                try:   
                    num = float(input("\nWhat is the second number\n:"))
                    #handle divide by zero exception
                    if op == "/" and num == 0:
                        print("\nError: dividing by zero\n")
                        num = None
                except ValueError:
                    print("\nThats not a number")

            if op == "+":
                result = val + num
            elif op == "-":
                result = val - num
            elif op == "*":
                result = val * num
            elif op == "/":
                result = val / num
            else:
                print("\nsomething went wrong in choosing the operator")

            print(val, op, num, "=", result)



            result_str = f"{val} {op} {num} = {result}"

            past_calc.append(result_str)

            val = result

        see_past = input("Do you want to see all the previous calculations?(y/n)")
        if see_past in ("y", "yes"):
            for item in past_calc:
                print(item)

        



    #temperature conversion   
    elif mode == 2:
    

        # this defines the unit map
        unit_map = {
        "1": "celsius",
        "2": "fahrenheit",
        "3": "kelvin",
        "4": "rankine"
                    }

        #this defines the functions
        def c_to_f(c): return (c * (9/5)) + 32
        def f_to_c(f): return (5/9)*(f-32)
        def c_to_k(c): return c + 273.15
        def k_to_c(k): return k - 273.15
        def c_to_r(c): return (c * (9/5)) + 491.67
        def r_to_c(r): return (r-491.67) * (5/9)
        def f_to_k(f): return ((f - 32) * (5/9))+ 273.15
        def k_to_f(k): return ((k-273.15) * 1.8) + 32
        def f_to_r(f): return f + 459.67
        def r_to_f(r): return r - 459.67
        def k_to_r(k): return k * (9/5)
        def r_to_k(r): return r * (5/9)

        #this builds a map which connects the units chosen to the function it should use
        #this is another dictionary
        converts = {
                ("1", "2"): c_to_f,  # Celsius → Fahrenheit
                ("2", "1"): f_to_c,  # Fahrenheit → Celsius
                ("1", "3"): c_to_k,  # Celsius → Kelvin
                ("3", "1"): k_to_c,  # Kelvin → Celsius
                ("1", "4"): c_to_r,  # Celsius → Rankine
                ("4", "1"): r_to_c,  # Rankine → Celsius
                ("2", "3"): f_to_k,  # Fahrenheit → Kelvin
                ("3", "2"): k_to_f,  # Kelvin → Fahrenheit
                ("2", "4"): f_to_r,  # Fahrenheit → Rankine
                ("4", "2"): r_to_f,  # Rankine → Fahrenheit
                ("3", "4"): k_to_r,  # Kelvin → Rankine
                ("4", "3"): r_to_k   # Rankine → Kelvin
            }

    
        print("\nThis is the temperature converter\n")
        print("\nWhich unit would you like to convert from?\n")

            #this is the from_choice section

            #print all of the options in unit_map
        for key, name in unit_map.items():
            print(f" {key}: {name}")

        from_choice = input("\nChoose the number for the temperature unit you want to convert from (1,2,3,4):\n").strip()

        while from_choice not in unit_map:
                print("\nThat's not one of the options!")
                from_choice = input("\nChoose the number for the temperature unit you want to convert from (1,2,3,4):\n").strip()
            

        # get the numeric value that we want converted
        
        value = None
        while value == None:
            try:
                value = float(input(f"\nPlease enter the temperature in {unit_map.get(from_choice)} that you want converted\n"))
            except ValueError:
                print("\nThats not a number")
        #this is the to_choice section
        
        #need to make it so that once a unit is selected it doesnt show up
        #for the next unit being selected

        print("\nwhich temperature unit would you like to convert to?\n")
        for key, name in unit_map.items():
            if key == from_choice:
                continue
            print(f" {key}: {name}")
            
        #make a new list which stores the unit_map keys which havent been selected
        remaining_items = []

        for key in unit_map.keys():
            if key == from_choice:
                continue
            remaining_items.append(key)

            #this joins the items from the list into a string and separates them with a comma
        remaining_choices = ", ".join(remaining_items)

        to_choice = input(f"\nChoose the number for temperature unit you want to convert to ({remaining_choices}): \n").strip()

        while to_choice not in unit_map or from_choice == to_choice:
            print("\nThat's not one of the options")
            to_choice = input(f"\nChoose the number for temperature unit you want to convert to {remaining_choices}: \n").strip()


        

        # need to combine from_choice and to_choice to use the desired formula
        func = converts.get((from_choice, to_choice))

        if func == None:
            raise Exception("\nError: there is no conversion defined for that unit pair")
        result = func(value)

        print(
            f"\n{value} {unit_map.get(from_choice)}"
            f" is {result} {unit_map.get(to_choice)}"
                )
        
    ex = input("\nIf you want to exit the application type 'exit' \n" \
    "or else just hit enter.\n")
    exit= []
    exit.append(ex)
    if "exit" in exit:
        break







   
   







    

