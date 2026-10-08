# simple calculator program:

operator = input("choose an operator:")
num1= int(input("enter the first number:"))
num2= int (input("enter the second number:"))




if operator == "+":
    result = num1 + num2
    print (round(result, 3))

if operator == "-":
    result = num1 - num2
    print(round(result, 3))

    if operator == "*":
        result = num1 * num2
        print(round(result, 3))

if operator == "/":
    result = num1 / num2
    print(round(result, 3))

else:
    print(f"{operator} is not a valid operator")
