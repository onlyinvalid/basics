keepGoing = True

while keepGoing:
    

    num = None

    while num is None:
        try :
            num = int(input("Enter number here to see if even or odd: "))
        except ValueError:
            print("Thats not a number, try again.")
        

    if num % 2 == 0:
        ans = "even"
    else :
        ans = "odd"

    print("the number is: ", ans)

    

    while True:
        
        
        goOrNo = input("Do you want to try another number? (Y/N)").strip().upper()
        

        if goOrNo == 'N':
           keepGoing = False 
           break
        elif goOrNo == 'Y':
            break    
        else:
            print("Type Y or N please")

