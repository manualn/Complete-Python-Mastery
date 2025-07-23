#ALGORITHM
# 1)Start
# 2)Input comma seperated 3 numbers and store it in a variable
# called input_number
# 3)Use split to split the input_number at comma and store
# it in a variable named numbers
# 4)Store the three variables in three different variables
# named a,b and c
# 5)Define a function second_largest(a,b,c)
# 6)Start with an if loop considering "a" as second largest
# number and write the conditions using "and" and "or"
# 7)Then Return a
# 8)then elif condition consider b as second largest number
# 9)then return b
# 10)Else return c
# 11)Call function and pass a,b and c in it and store it in 
# variable called largest_second
# 12)Print largest_second
# 13)End

input_number = input("Enter comma-separated 3 numbers: ")

numbers = input_number.split(",")
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

def second_largest(a,b,c):
    if (a > c and a < b) or (a > b and a < c):
        return a
    elif (b > c and b < a) or (b < c and b > a):
        return b
    else:
        return c
    
largest_second = second_largest(a,b,c)
print(f"Second largest number: {largest_second}")

