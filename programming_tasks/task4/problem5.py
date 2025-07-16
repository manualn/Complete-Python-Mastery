# 5. Filter Even Numbers from a List
# Ask to enter comma seperated numbers
num = input("Enter comma seperated numbers: ")

all_numbers =[] #empty list to store all numbers

current = "" # Use temporary string to build each number character

# Go through each character in input
for ch in num:
    if (ch == ","):
        # When there is a comma, it means the 
        # current number is complete
        all_numbers.append(int(current))
        # Convert it to integer and add to list
        current = "" # reset it for next loop
    else:
        current += ch # keep adding if there is no comma

# this condition is to add last number
if current != "":
    all_numbers.append(int(current))

even_numbers =[] # a new list to store even numbers only

# Define function to get even numbers from a given numbers
def filter_evens(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])

# Call function and pass the list of all numbers
filter_evens(all_numbers)

# Print the result
print("even numbers: ", even_numbers)
