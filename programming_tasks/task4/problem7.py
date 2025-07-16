# 7. Find the Greater of Two Numbers
# Ask to input first number
x = int(input("Enter first number: "))
# Ask to input second number
y = int(input("Enter second number: "))

# define a function to find the greater of x and y
def greater(x,y):
    if (x > y):
    # If x is greater than y, return x
        return x    
    else:
    # if y is greater than x, return y
        return y

# Print the greater number
print(f"Greater number: {greater(x,y)}")