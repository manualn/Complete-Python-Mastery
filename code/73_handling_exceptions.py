try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age")

print("Execution continues")



try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")

print("Execution continues.")