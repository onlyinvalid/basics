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

    while op1 not in("+","-","*","/"):
        op1 = input("What operation do you want to use? (+,-,*,/)\n:")

        if op1 not in ("+","-","*","/"):
            print("That isnt one of the operations")


    num1 = 0

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
   
   print("This is the temperature converter")

   
   



    

