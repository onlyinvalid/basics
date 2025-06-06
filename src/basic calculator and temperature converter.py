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
mode = None

while mode not in (1,2):
    try: 
        mode = int(input("1: calculator \n2: temperature converter \n:"))
    
        if mode not in(1,2):
            print("That isn't one of the options")
    
    except ValueError:
        print("That isnt one of the options")

#calculator
if mode == 1:
   
    print("This is the calculator")

    op1 = None

    #loop to prevent wrong input of operator
    while op1 not in("+","-","*","/"):
        op1 = input("What operation do you want to use? (+,-,*,/)\n:")

        if op1 not in ("+","-","*","/"):
            print("That isnt one of the operations")


    num1 = 0

    #loopa to prevent wrong input of number
    while num1 == 0:
        try:
            num1 = float(input("What is the first number\n:"))

        except ValueError:
            print("Thats not a number")

    num2 = 0
    while num2 == 0:
        try:   
            num2 = float(input("What is the second number\n:"))

        except ValueError:
            print("Thats not a number")


    if op1 == "+":
        val = num1 + num2
    elif op1 == "-":
        val = num1 - num2
    elif op1 == "*":
        val = num1 * num2
    elif op1 == "/":
        val = num1 / num2
    else:
        print("something went wrong in choosing the operator")

    print(num1, op1, num2, "=", val)
       

#temperature conversion   
elif mode == 2:
   
   #celcius, fahrenheit, kelvin, rankine
   #c to f
   #f to c
   #c to k
   #k to c
   #c to r
   #r to c
   #f to k
   #k to f
   #f to r
   #r to f
   #k to r
   #r to k

    # this defines the unit map
   unit_map = {
       "1": "celcius",
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

   
   print("This is the temperature converter")
   print("Which unit would you like to convert from?")

    #this is the from_choice section

    #print all of the options in unit_map
   for key, name in unit_map.items:
       print(f" {key}: {name}")

   from_choice = input("Choose the number for the from unit: ").strip()

   while from_choice not in unit_map:
        print("That's not one of the options!")
        from_choice = input("Choose the number for the from unit: ").strip()
    

   # get the numeric value that we want converted
   
   value = None
   while value == None:
    try:
        value = float(input(f"Please enter the temperature in {name} that you want converted\n"))
    except ValueError:
        print("Thats not a number")
   #this is the to_choice section
    


   #need to make it so that once a unit is selected it doesnt show up
   #for the next unit being selected

   print("which unit would you like to convert to?")
   for key, name in unit_map.items:
       if key == from_choice:
           continue
       print(f" {key}: {name}")
    
   to_choice = input("Choose the number for the to unit: ").strip()

   while from_choice not in unit_map or from_choice == to_choice:
       print("That's not one of the options")
       to_choice = input("Choose the number for the to unit: ").strip()


   

   # need to combine from_choice and to_choice to use the desired formula
   func = converts.get(from_choice, to_choice)

   result = func(value)

   print(
       f"{value} {from_choice}"
       f"is {result} {to_choice}"
         )






   
   







    

