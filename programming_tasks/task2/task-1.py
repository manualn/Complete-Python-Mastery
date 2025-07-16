first_number = float(input("first number: "))
operator = input("operator: ")
second_number = float(input("Second number: "))

result = None
if (operator == "+"):
    result = first_number + second_number
elif (operator == "-"):
    result = first_number - second_number
elif (operator == "*"):
    result = first_number * second_number
elif (operator == "/"):
    try:
        result = first_number / second_number
    except(ZeroDivisionError):
        print("Cannot be divided by zero")

else:
    print("invalid operator")


if result != None:
    print("The result is: ", result)

