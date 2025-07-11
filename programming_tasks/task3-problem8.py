#8. Sum All Numbers in a List
# Ask to input comma seperated numbers
num = input("enter comma seperated numbers: ")
# split the number by commas and 
# convert each string into an integer using map and
# store in a list
numbers = list(map(int,num.split(",")))

# Define a function to get the sum of numbers in list
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n # add each number to total
    return total

# print the result
print(f"Sum: {sum_list(numbers)}")

