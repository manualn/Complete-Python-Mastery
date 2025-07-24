# ALGORITHM
# 1) Start
# 2) Create an empty list called numbers
# 3) start with a for loop to input 6 numbers
# 4) Prompt the user to enter a number and store it in variable num
# 5) Convert num to integer and append it to numbers list
# 6) check if i is in range(1,7)
# 7) If Yes, go to Step 5
# 8) Else, go to Step 9
# 9) Define a function called remove_duplicates that takes a list lst as input
# 10) Inside the function, create an empty list called result
# 11) Create a loop for each item in lst
# 12) Check if item is not in result using an if condition
# 13) If True, go to Step 14
# 14) Append item to result
# 15) Repeat Step 12 for the next item
# 16) Return result from the function
# 17) Call the function remove_duplicates and pass the numbers list and store it in variable called unique
# 18) Print unique
# 19) End



numbers = []
for i in range(1,7):
    num = int(input(f"enter number {i}: "))
    numbers.append(num)


def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

unique = remove_duplicates(numbers)
print(f"Output: {unique}")