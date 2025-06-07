print("This is a palindrome checker")

while True:
    
    value = None
    while value == None:
        value = input("\nenter the potential palindrome here: ")
        if len(value) <= 1:
            print("try again")
            value = None


    reverse_value = value[::-1]

    if value == reverse_value:
        print("\nthis is a palindrome")
    else:
        print("\nthis is not a palindrome")

    ex = input("\ndo you want to exit the application?(y/n): ")
    if ex == "y":
        break
    