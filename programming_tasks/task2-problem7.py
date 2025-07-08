# 7. Add All Numbers in a List
input_str = input("Enter comma-separated numbers: ")
# Create an empty list to store the parsed numbers
values = []

# Temporary string to build each number character by character
current = ""

# Loop through each character in the input string
for ch in input_str:
    if ch == ",":
        # If a comma is found, convert current string to int and add to list
        values.append(int(current))
        current = ""  # Reset current for the next number
    else:
        # If not a comma, add the character to the current number string
        current += ch

        
# Add the last number after the loop (if it's not empty)
if current != "":
    values.append(int(current))

print(sum(values))