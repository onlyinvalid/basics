
print("this program will carry out a mathematical operation of your choosing")

try:
    num1 = float(input("enter first number here: \n"))
    num2 = float(input("enter second number here: \n"))
    operand1 = input("enter the operation you want(+,-,*,/)\n")

    if operand1 == '+' :
        print("the answer is : " , (num1 + num2))
    elif operand1 == '-':
        print("the answer is : " , (num1 - num2))
    elif operand1 == '*':
        print("the answer is : " , (num1 * num2))
    elif operand1 == '/': 
        print("the answer is : " , (num1 / num2))
    else :
        raise ValueError("invalid operator")

except ValueError as ve:
    print("Error:", ve)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Unknown Error: " , e)