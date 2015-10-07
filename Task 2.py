num1 = float(input("Please enter first number: "))
num2 = float(input("Please enter second number: "))
operation = input("Enter the operator: ")

if operation == "+":
    print (num1 + num2)

elif operation == "-":
    print (num1 - num2)

elif operation == "*":
    print (num1 * num2)

elif operation == "/":
    print (num1 / num2)

else:
    print ("Error, invalid oporator")
    

