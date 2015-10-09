while True: #loop forever until told to break (quit)

    num1 = input("Please enter first number (Or q to quit): ") # ask user for input & store input in variable num1

    if num1 == "q": # if user entered q break out of the loop and let program end
        break

    num1 = float(num1) # converts user input to a decimal number
    num2 = float(input("Please enter second number: ")) # ask's user for input and converts to decimal number and stores in variable num2
    operation = input("Enter the operator: ") # Ask's the user to choose the opartion (*,/,+,-) and storing result in variable operation

    if operation == "+":
        print (num1 + num2) # is the user chose + as a operator add num1 and num2 and output the result 

    elif operation == "-":
        print (num1 - num2) # is the user chose - as a operator subtract num2 from num1 and output the result

    elif operation == "*":
        print (num1 * num2) # is the user chose * as a operator mmultiply num1 and num2 and output the result

    elif operation == "/":
        print (num1 / num2) # is the user chose / as a operator divide num1 by num2 and output the result
    
    else:
        print ("Error, invalid oporator") # if the user chose an unrecognised key print error message
